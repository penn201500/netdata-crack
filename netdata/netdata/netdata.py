#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from time import strftime
import os
import shutil
import json


def parse_proc_net_dev():
    # only 1 net device exists, such as eth0
    receive_bytes = []
    transimit_bytes = []
    with open("/proc/net/dev", "r") as f:
        lines = f.read().splitlines()
        for i in lines:
            if ('eth0' in i) and (':' in i):
                receive_bytes.append(int((i.split(':')[1].split()[0])))
                transimit_bytes.append(int((i.split(':')[1].split()[9])))
    return(receive_bytes, transimit_bytes)


if __name__ == '__main__':
    # for i in range(5):
    while 1:
        data = []
        (rbytes, tbytes) = parse_proc_net_dev()
        time.sleep(1)
        (rbytes_new, tbytes_new) = parse_proc_net_dev()
        # rbytes[:] = [float(x)/1024/8 for x in rbytes]
        # tbytes[:] = [float(x)/1024/8 for x in tbytes]
        in_flow = float(rbytes_new[0] - rbytes[0])/1024/8
        out_flow = float(tbytes_new[0] - tbytes[0])/1024/8
        # print parse_proc_net_dev()
        # print rbytes
        # print tbytes
        time_now = strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        timestamp = strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        # if os.path.isfile('flow_stat.json'):
        #     shutil.copy('flow_stat.json', 'flow_stat-'+timestamp+'.json')
        data.append({time_now:{"in_flow":in_flow, "out_flow":out_flow}})
        with open("./flow_stat.json", "w") as f:
            f.truncate()
            json.dump(data, f)
