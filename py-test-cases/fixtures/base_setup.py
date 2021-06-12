#------------------------------------------------------------------------------
# Returns the currently active setups. 
#------------------------------------------------------------------------------
import os
import pytest
from kubernetes import client, config

@pytest.fixture
def running_pods () :
    try :
        config.load_kube_config()
    except:
        return None

    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

    return ret

@pytest.fixture
def kne () :
    try :
        kne_bin_path = os.environ['KNE_BIN_PATH'] 
    except :
        kne_bin_path = None

    return kne_bin_path
