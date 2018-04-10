#nohup geth --rpc --rpccorsdomain "*" --bootnodes $(curl https://raw.githubusercontent.com/Hatuw/deployBC/master/ethereum/bootnode) &


ansible eth -m shell -a "nohup geth --rpc --rpccorsdomain \'*\' --bootnodes \$(curl https://raw.githubusercontent.com/Hatuw/deployBC/master/ethereum/bootnode) >> geth.log" -T 1 -f 10