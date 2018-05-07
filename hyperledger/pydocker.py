# -*- coding: utf-8 -*-
import docker

BASE_URL = "unix://var/run/docker.sock"

client = docker.DockerClient(base_url=BASE_URL, version='auto', timeout=5)

containers = client.containers.list()

for item in containers:
    print(item.attrs['Config'])
    break
    # print(item.logs())
