import sys
from gnmi.structures import SubscribeOptions
from gnmi import capabilites, get, delete, replace, update, subscribe
from gnmi.exceptions import GrpcDeadlineExceeded

def stat(target, paths) :
    stat_list = []
    try:
        for notif in subscribe(target, paths, auth=("admin", ""),
            options=SubscribeOptions(mode="once")):
            prefix = notif.prefix
            for update in notif.updates:
                value = update.get_value()
                data = "%s:%s" %(prefix + update.path, value)
                if (data not in stat_list) :
                    stat_list.append(data)
        # end for
    except :
        pass
    
    return stat_list

if __name__ == "__main__" :
    if (len(sys.argv) < 3) :
        print("usage : argv[0] <target> <comma seperated list of paths>")
    else :
        target = sys.argv[1]
        path = sys.argv[2]
        retval = stat(target=target, paths=[path])
        for v in retval:
            print(v)
