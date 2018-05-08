# -*- coding: utf-8 -*-
import os
import json
import matplotlib.pyplot as plt

LOGS_DIR = "./logs"

stats_dir = os.path.join(LOGS_DIR, 'stats')

stats_files =[os.path.join(stats_dir, file) for file in os.listdir(stats_dir)]

data_dict = {}

for file in stats_files:
    with open(file, 'r') as f_in:
        json_dict = json.load(f_in)
    if json_dict['name'] in data_dict.keys():
        data_dict[json_dict['name']].append(json_dict)
    else:
        data_dict[json_dict['name']] = [json_dict]
    # print(json_dict['name'], end=':')
    # print(json_dict['cpu_stats']['cpu_usage']['total_usage'])

for key in data_dict.keys():
    data_dict[key].sort(key=lambda x: x['read'])
    cpu_usage = []
    for item in data_dict[key]:
        cpu_usage.append(item['cpu_stats']['cpu_usage']['total_usage'])
    # plt.plot(cpu_usage)
    # plt.show()
