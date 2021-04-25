#!/usr/bin/python3
import os
import sys

import logging
import grpc
import common_pb2
import interface_pb2
import interface_pb2_grpc
import bgpd_pb2
import bgpd_pb2_grpc

import get_demon

def status_to_string(status):
    if status == common_pb2.StatusResponse.SUCCESS:
        return "SUCCESS"
    elif status == common_pb2.StatusResponse.FAILURE:
        return "FAILURE"
    else:
        return "UNSPECIFIED"

def demon_up(proto, pod_name) :
    get_pid = "kubectl exec %s -- pidof InterfaceManager" %(pod_name)
    f = os.popen(get_pid)
    pid = f.read().rstrip()
    f.close()

    get_demon = "kubectl exec %s -- cat /proc/%s/maps | grep -i %s"\
            %(pod_name, pid, proto)
    f = os.popen(get_demon)
    retval = f.read().rstrip()
    f.close()

    return retval

def run(pod_ip,
        pod_name,
        namespace,
        listening_port_no,
        config_count,
        interface_id,
        interface_id_step,
        mac_address,
        mac_address_step,
        ip_address,
        ip_address_step,
        gw,
        gw_step,
        mask,
        bgp_peer_index,
        bgp_peer_id,
        bgp_as_number,
        dut_ip,
        bgp_peer_index_step,
        bgp_peer_id_step,
        bgp_as_number_step,
        dut_ip_step,
        bgp_route_index,
        bgp_route_ip,
        bgp_route_mask,
        bgp_nexthop_ip,
        bgp_route_count,
        bgp_route_index_step,
        bgp_route_ip_step,
        bgp_nexthop_ip_step,
        bgp_route_count_step,
    ):
    connect_string = pod_ip + ':' + str(listening_port_no)
    print("Connecting to %s :" %(connect_string))

    with grpc.insecure_channel(connect_string) as channel:

        iface_stub = interface_pb2_grpc.InterfaceStub(channel)
        bgp_stub = bgpd_pb2_grpc.BGPStub(channel)
        port = 1

        interface = interface_pb2.InterfaceConfig(
            interface_id=interface_id,
            mac=mac_address,
            ip=ip_address,
            mask=mask,
            gw=gw)

        interface_step = interface_pb2.InterfaceConfig(
            interface_id=interface_id_step,
            mac=mac_address_step,
            ip=ip_address_step,
            gw=gw_step)

        bgp_peer = bgpd_pb2.BGPPeerConfig(
            peer_index=bgp_peer_index,
            peer_id=bgp_peer_id,
            as_number=bgp_as_number,
            dut_ip=dut_ip,
            interface=interface,
            type=bgpd_pb2.BGPPeerConfig.SessionType.EBGP)

        bgp_peer_step = bgpd_pb2.BGPPeerConfig(
            peer_index=bgp_peer_index_step,
            peer_id=bgp_peer_id_step,
            dut_ip=dut_ip_step,
            as_number=bgp_as_number_step,
            interface=interface_step)

        bgp_route = bgpd_pb2.BGPRouteConfig(
            peer_index=bgp_peer_index,
            route_index=bgp_route_index,
            route=bgp_route_ip,
            route_mask=bgp_route_mask,
            nexthop=bgp_nexthop_ip,
            route_count=bgp_route_count)

        bgp_route_step = bgpd_pb2.BGPRouteConfig(
            peer_index=bgp_peer_index_step,
            route_index=bgp_route_index_step,
            route=bgp_route_ip_step,
            route_mask=bgp_route_mask,
            nexthop=bgp_nexthop_ip_step,
            route_count=bgp_route_count_step)

        add_request=common_pb2.ConfigRequest(
            port_id=port,
            type=common_pb2.ConfigRequest.ADD
        )

        response = iface_stub.ConfigureInterface(
            interface_pb2.InterfaceConfigRequest(
                request=add_request,
                config=interface,
                count=config_count,
                step=interface_step)
        )
        print("Interface creation: " + status_to_string(response.status))

        response = bgp_stub.StartService(common_pb2.StartRequest(port_id=port))
        print("BGPD daemon start: " + status_to_string(response.status))

        response = bgp_stub.ConfigureService(
            bgpd_pb2.BGPConfigRequest(
                request=add_request,
                config=bgpd_pb2.BGPConfig(peer_config=bgp_peer),
                count=config_count,
                step=bgpd_pb2.BGPConfig(peer_config=bgp_peer_step)
            )
        )
        print("Configure BGP Peer(s): " + status_to_string(response.status))

        response = bgp_stub.ConfigureService(
            bgpd_pb2.BGPConfigRequest(
                request=add_request,
                config=bgpd_pb2.BGPConfig(route_config=bgp_route),
                count=config_count,
                step=bgpd_pb2.BGPConfig(route_config=bgp_route_step)
            )
        )
        print("Configure BGP Route Range: " + status_to_string(response.status))

        retval = get_demon.demon_up(pod_name, 'bgp', namespace)
        if (retval):
            print('bgpd started %s %s %s' %(pod_ip, pod_name, namespace))
            print(retval)
        else :
            print("WARNING: bgp may not have started properly!")



if __name__ == '__main__':
    logging.basicConfig()
   
    if (len(sys.argv) < 5) :
        print("usage:\t%s <pod_ip1> <pod_ip2> <pod_name1> <pod_name2> <namespace>" %(sys.argv[0]))
        sys.exit(0)
    else :     
        pod_ip1 = sys.argv[1]
        pod_ip2 = sys.argv[2]
        pod_name1 = sys.argv[3]
        pod_name2 = sys.argv[4]
        namespace = None

        if (len(sys.argv) == 6):
           namespace = sys.argv[5]
           
        config_count = 10

    # BGP router 1
    run(pod_ip=pod_ip1,
        pod_name=pod_name1,
        namespace=namespace,
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

    run(pod_ip=pod_ip2,
        pod_name=pod_name2,
        namespace=namespace,
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

