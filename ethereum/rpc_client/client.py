import time
from web3 import Web3, HTTPProvider

# pre-define the info of private node
HOST = r"127.0.0.1"
PORT = r"8545"
ADDR = r"0xdb8086002d43605b7118a3069818bce5212dc60d"

# connect to the private node
w3 = Web3(HTTPProvider("http://{}:{}".format(HOST, PORT)))

print(w3.admin.peers)
