import time
import pytest
from kubernetes import watch, client

from fixtures.base_setup import running_pods, kne

from bgp_lib import bgp
from utils.kne import kne_execute
from utils.common_cmd import watch
from utils import gnmic

def test_running_pod (running_pods, kne, config) :
    """ The objective of this test cases is to verify the following
        1. kne utility can deploy a simple topology in the system.
        2. Two basic Ixia BGP sessions can be configured on the top of the 
           above topology.
        3. Gnmi utility can fetch BGP statistics from Ixia BGP pods.
           This utility is used several times (depending on stress_count) to 
           fetch the stats from BGP pods.
        4. Value returned by the statistics is not the concern of this test case.

    Args:
        running_pods (list): Detail list of all the pods on all the namespaces 
            in this system

        kne (string): The path of the kne_cli utility
        config (string): The path of the config (topology) file used by kne_cli.

    Returns:
        None
    """
    if (running_pods) :
        if (kne) :
            kne_execute(kne=kne, command="create", filename=config)
            ip_list = watch(namespace="regression", time_out=60, count=2)

            if (ip_list) :
                print('IPs obtained are : %s' %ip_list)
            else :    
                pytest.fail("All pods are not up.")

            time.sleep(5)

            # 10 bgp routers per pod
            config_count = 10

            # Configure and run BGP router on pod 1 
            bgp.run(pod_ip=ip_list[0][0],
                pod_name=ip_list[0][1],
                namespace=ip_list[0][2],
                listening_port_no=50061,
                config_count=config_count,
                interface_id=1,
                interface_id_step=1,
                mac_address='00:16:01:00:00:01',
                mac_address_step='00:00:01:00:00:00',
                ip_address='1.1.1.2',
                ip_address_step='0.0.0.1',
                gw='1.1.1.1',
                gw_step='0.0.0.0',
                mask=24,
                bgp_peer_index=1,
                bgp_peer_id='196.5.6.1',
                bgp_as_number=1000,
                dut_ip='1.1.1.1',
                bgp_peer_index_step=1,
                bgp_peer_id_step='0.0.0.0',
                bgp_as_number_step=0,
                dut_ip_step='0.0.0.0',
                bgp_route_index=1,
                bgp_route_ip='11.11.1.0',
                bgp_route_mask=0,
                bgp_nexthop_ip='1.1.1.2',
                bgp_route_count=2,
                bgp_route_index_step=1,
                bgp_route_ip_step='1.0.0.0',
                bgp_nexthop_ip_step='0.0.0.1',
                bgp_route_count_step=0,
            )

            time.sleep(5)  

            # Configure and run BGP router on pod 2 
            bgp.run(pod_ip=ip_list[1][0],
                pod_name=ip_list[1][1],
                namespace=ip_list[1][2],
                listening_port_no=50061,
                config_count=config_count,
                interface_id=1,
                interface_id_step=1,
                mac_address='00:56:01:00:00:01',
                mac_address_step='00:00:01:00:00:00',
                ip_address='1.1.1.1',
                ip_address_step='0.0.0.1',
                gw='1.1.1.2',
                gw_step='0.0.0.0',
                mask=24,
                bgp_peer_index=1,
                bgp_peer_id='199.5.6.1',
                bgp_as_number=1000,
                dut_ip='1.1.1.2',
                bgp_peer_index_step=1,
                bgp_peer_id_step='0.0.0.0',
                bgp_as_number_step=0,
                dut_ip_step='0.0.0.0',
                bgp_route_index=1,
                bgp_route_ip='12.12.1.0',
                bgp_route_mask=0,
                bgp_nexthop_ip='1.1.1.5',
                bgp_route_count=2,
                bgp_route_index_step=1,
                bgp_route_ip_step='1.0.0.0',
                bgp_nexthop_ip_step='0.0.0.1',
                bgp_route_count_step=0,
            )

            time.sleep(5)

            stat_error_count = 0
            stress_count = 1
            for i in range(stress_count) :
                for demon in [ip_list[0][0] + ':' + '50051',  ip_list[1][0] + ':' + '50051'] :
                    print('getting statistics from stat demon %s' %(demon))
                    retval = gnmic.stat(demon, ['/protocols/bgp/'])
                    if (retval) :
                        for v in retval :
                            print("\t%s"%(v))
                    else :
                        stat_error_count += 1

            if (stat_error_count):
                 pytest.fail("not all bgp instances are up an running")

            # Delete the pods
            kne_execute(kne=kne, command="delete", filename=config)
        else :
            pytest.fail("kne utility is not available.")
    else :
        pytest.fail("Failed to get any running pods.")
