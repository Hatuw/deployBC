# -*- coding: utf-8 -*-

import os
import re

log_file = './logs/console-logs/orderer.example.com.logs'

assert os.path.exists(log_file), "logs does not exist"

logs_data = []
with open(log_file, 'r') as f_in:
    tmp_log = f_in.readlines()

for item in tmp_log:
    if re.match(r'.+(\[Start\]|\[End\])', item):
        logs_data.append(item)
del tmp_log

for i in range(10):
    print(logs_data[i], end='')
