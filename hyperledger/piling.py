# -*- coding:utf-8 -*-
import os
import re


# set the project dir
GOPATH = os.environ.get("GOPATH")
assert GOPATH, '$GOPATH not set'
PROJECT_DIR = '{}/src/github.com/hyperledger/fabric'.format(GOPATH)

peer_dir = os.path.join(PROJECT_DIR, 'peer')

go_files = []
for root, dirs, files in os.walk(peer_dir):
    for file in files:
        if re.match(r'(\w+[^(_test)]\.go$)', file):
            print(file)
            fullpath = os.path.join(root, file)
