# -*- coding: utf-8 -*-
import os
import json
import time
import shutil
import docker
from threading import Thread


class Client():
    def __init__(self, **kwargs):
        self._BASE_URL = "unix://var/run/docker.sock"
        self.LOGS_DIR = "./logs"
        # clean database
        if 'clean_db' in kwargs.keys():
            if kwargs['clean_db']:
                self.clean_db()
        # connect to docker
        self.client = self.connect()

    def connect(self):
        client = docker.DockerClient(
            base_url=self._BASE_URL,
            version='auto',
            timeout=5)
        return client

    def print_json(self, json_data):
        print(json.dumps(json_data, indent=4))

    def clean_db(self):
        try:
            # os.removedirs(self.LOGS_DIR)
            shutil.rmtree(self.LOGS_DIR, ignore_errors=True)
        except Exception as e:
            print(e)
            return False
        return True

    def collect_logs(self, container):
        """
        :params: container: docker container object
        """
        # the container name in fabric is "/***.***.com", need to fix
        container_name = container.attrs['Name'][1:]
        logs_dir = os.path.join(self.LOGS_DIR, 'console-logs')
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        logs_data = container.logs().decode('utf-8')

        # define the output filename and path
        out_file = os.path.join(
            logs_dir,
            '{}.logs'.format(container_name))

        # write the output
        with open(out_file, 'w') as logs_out:
            logs_out.write(logs_data)
        return True

    def get_stats(self, container, **kwargs):
        """
        :params:
            container: the docker container object
            decode (bool): If set to true,
                stream will be decoded into dicts on the fly.
                False by default.
            stream (bool): If set to false,
                only the current stats will be returned instead
                of a stream. False by default
        """
        save = kwargs['save'] if 'save' in kwargs.keys() else False
        stats = container.stats(decode=False, stream=False)

        if save:
            # init the logs dir
            logs_dir = os.path.join(self.LOGS_DIR, 'stats')
            if not os.path.exists(logs_dir):
                os.makedirs(logs_dir)
            # use md5 to define the file's name
            import hashlib
            md5 = hashlib.md5()
            md5.update(str(stats).encode('utf-8'))
            filename = md5.hexdigest()
            # log
            with open(os.path.join(logs_dir, filename), 'w') as logs_out:
                logs_out.write(json.dumps(stats, indent=4))
            return True
        else:
            # self.print_json(stats)
            return stats


def main():
    # new a client and connect to docker
    client = Client(clean_db=True)
    docker_client = client.client
    containers = docker_client.containers.list()

    for item in containers:
        client.collect_logs(item)

    # for _ in range(5):
    #     for item in containers:
    #         # print(item.attrs['Name'])

    #         # use threading to reduce waiting time
    #         t = Thread(
    #             target=client.get_stats,
    #             args=(item, ),
    #             kwargs={'save': True})
    #         t.start()
    #     time.sleep(1)


if __name__ == '__main__':
    main()
