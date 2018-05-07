# -*- coding: utf-8 -*-
import os
import docker

BASE_URL = "unix://var/run/docker.sock"
LOGS_DIR = "./logs"

client = docker.DockerClient(base_url=BASE_URL, version='auto', timeout=5)

containers = client.containers.list()

for item in containers:
    container_name = item.attrs['Name'][1:]
    print(container_name)
    logs_data = item.logs().decode('utf-8')
    out_file = os.path.join(LOGS_DIR, '{}.logs'.format(container_name))
    with open(out_file, 'w') as logs_out:
        logs_out.write(logs_data)
