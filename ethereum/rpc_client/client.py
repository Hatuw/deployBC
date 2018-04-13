# -*- coding:utf-8 -*-
# import time
import json
from web3 import Web3, HTTPProvider
# docs of web3: https://pypi.python.org/pypi/web3/2.3.0

# pre-define the info of private node
# HOST = r"127.0.0.1"
HOST = r"172.18.196.1"
PORT = r"8545"
ADDR = r"0xdb8086002d43605b7118a3069818bce5212dc60d"

# connect to the private node
w3 = Web3(HTTPProvider("http://{}:{}".format(HOST, PORT)))


def __print_json(json_data):
    print(json.dumps(json_data, indent=4))


peer_info = w3.admin.peers
if peer_info:
    __print_json(w3.admin.peers)
print(len(w3.admin.peers))
