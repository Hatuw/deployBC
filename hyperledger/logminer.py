# -*- coding: utf-8 -*-

import os
import re

log_file = './logs/console-logs/orderer.example.com.logs'
out_log = './logs/filter.log'

assert os.path.exists(log_file), "logs does not exist"


def filter_logs(src_log, out_name='./logs/filter.log'):
    logs_data = []
    with open(src_log, 'r') as f_in:
        tmp_log = f_in.readlines()

    for item in tmp_log:
        if re.match(r'.+(\[Start\]|\[End\])', item):
            logs_data.append(item)
    del tmp_log

    with open(out_name, 'w') as f_out:
        for item in logs_data:
            f_out.write(item)
    return True

filter_logs(src_log=log_file)

with open(out_log, 'r') as logs_in:
    logs_data = []
    for line in logs_in.readlines():
        logs_data.append(line.strip())


for item in logs_data[1500:2500]:
    # print(item)
    try:
        ret = re.findall(r'(\[Start\].+\(.*\)|\[End\].+\(.*\))', item)[0]
        time = re.findall(r'2018.+UTC', item)[0]
        print(time, ret)
    except Exception as e:
        print(item, e)
        continue
