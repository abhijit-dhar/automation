import pytest
from kubernetes import watch, client

from fixtures.base_setup import running_pods, kne
from utils.kne import kne_execute
from utils.common_cmd import watch

def test_running_pod (running_pods, kne, config) :
    if (running_pods) :
        if (kne) :
            kne_execute(kne=kne, command="create", filename=config)
            ip_list = watch(namespace="regression", time_out=60, count=2)

            if (ip_list) :
                print('IPs obtained are : %s' %ip_list)

            #kne_execute(kne=kne, command="delete", filename=config)
        else :
            pytest.fail("kne utility is not available.")
    else :
        pytest.fail("Failed to get any running pods.")
