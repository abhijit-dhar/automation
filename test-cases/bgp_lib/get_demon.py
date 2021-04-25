#!/usr/bin/python3
import os
import sys

def demon_up(pod_name, proto, ns=None) :
    if (ns) :
        get_pid = "kubectl exec %s -n %s -- pidof InterfaceManager"\
            %(pod_name, ns)
    
        f = os.popen(get_pid)
        pid = f.read().rstrip()
        f.close()

        get_demon = "kubectl exec %s -n %s -- cat /proc/%s/maps | grep -i %s"\
            %(pod_name, ns, pid, proto)
    else :
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

if __name__ == '__main__':
    if (len(sys.argv) < 3) :
        print("usage:\t%s <pod_name> <protocol> <namespace>" %(sys.argv[0]))
        sys.exit(0)
    else :
        if (len(sys.argv) == 3):
            pod_name = sys.argv[1]
            proto = sys.argv[2]
            ns = None
        else :
            pod_name = sys.argv[1]
            proto = sys.argv[2]
            ns = sys.argv[3]

        retval = demon_up(pod_name=pod_name, proto=proto, ns=ns) 
        print(retval)
        sys.exit(0)
