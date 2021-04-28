import sys
from gnmi.structures import SubscribeOptions
from gnmi.api import capabilites, get, delete, replace, update, subscribe
from gnmi.exceptions import GrpcDeadlineExceeded

def stat(target, paths) :
    """This function is used to fetch statistics from ixia pods using
    gnmic.

    Args:
        target (string): This is generally a IP address (ip-addr:port) format.
        path (string): This is the specification statistics to be fetched.

    Returns:
        list: list of statistics element in the format as given below:
            [stats_name1:value, stats_name2:value, ...,]

    """
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


"""
This is a python module as well as a runnable program. To run it as a
standalone program and get its command line arguments just type the
command "./gnmic.py" at the command prompt.
"""
if __name__ == "__main__" :
    if (len(sys.argv) < 3) :
        print("usage : ./gnmic.py <target> <comma seperated list of paths>")
    else :
        target = sys.argv[1]
        path = sys.argv[2]
        retval = stat(target=target, paths=[path])
        for v in retval:
            print(v)
