from kubernetes import client, config

def watch (namespace, time_out, count) :
    config.load_kube_config()
    v1 = client.CoreV1Api()
    up_count = 0
    ip_list  = []
    while (time_out > 0) :
        ret = v1.list_pod_for_all_namespaces(watch=False)
        for i in ret.items:
            if (i.metadata.namespace == namespace) :
                if (i.status.phase.lower() == 'running') :
                    ip = i.status.pod_ip
                    if ip not in ip_list:
                        ip_list.append(ip)
                        up_count = len(ip_list)
                        
                    if (up_count == count) :
                        return ip_list
        time_out -= 1
    return None   
