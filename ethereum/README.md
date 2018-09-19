# Ethereum 测试链搭建

- 主链节点ip(MasterChain):
	172.18.196.1~9
- 侧链节点ip(SideChain):
	172.18.196.1~9

- install ethereum from PPA

*https://github.com/ethereum/go-ethereum/wiki/Installation-Instructions-for-Ubuntu*

```bash
sudo apt-get install software-properties-common
sudo add-apt-repository -y ppa:ethereum/ethereum
sudo apt-get update
sudo apt-get install ethereum
```

*注: 添加repository的时候,由于网络原因可能会失败.可能需要设置代理*


- 使用ansilbe批量安装ethereum：

```bash
ansible eth -m apt -f 10 -T 1 -o -s -a name=software-properties-common
ansible eth -m shell -f 10 -T 1 -o -s -a "add-apt-repository -y ppa:ethereum/ethereum"
ansible eth -m shell -f 10 -T 1 -o -s -a "apt-get update"
ansible eth -m apt -f 10 -T 1 -o -s -a name=ethereum
```

- 实验中使用的geth和go的版本信息如下：

> 
Geth
Version: 1.8.11-stable
Git Commit: dea1ce052a10cd7d401a5c04f83f371a06fe293c
Architecture: amd64
Protocol Versions: [63 62]
Network Id: 1
Go Version: go1.10
Operating System: linux
GOPATH=
GOROOT=/usr/lib/go-1.10

- 创世块(``genesis.json``)配置：

```json
{
    "config": {
        "chainId": 666,
        "homesteadBlock": 0,
        "eip155Block": 0,
        "eip158Block": 0
    },
    "alloc"      : {},
    "coinbase"   : "0x0000000000000000000000000000000000000000",
    "difficulty" : "0x100000",
    "extraData"  : "",
    "gasLimit"   : "0x2fefd8",
    "nonce"      : "0x0000000000000042",
    "mixhash"    : "0x0000000000000000000000000000000000000000000000000000000000000000",
    "parentHash" : "0x0000000000000000000000000000000000000000000000000000000000000000",
    "timestamp"  : "0x00"
}
```

- 使用ansible将创世块文件批量传送到节点上：

``ansible eth -m copy -f 10 -T 1 -a "src=./genesis.json dest=~/Documents/"``

- 使用ansible初始化创世块：

``ansible eth -m shell -f 10 -T 1 -a "geth init ~/Documents/genesis.json"``

- 使用ansible创建账户：

  - 先将密码文件传至节点：
    ``ansible eth -m copy -f 10 -T 1 -a "src=./password dest=~/Documents"``

  - 创建账户：
    ``ansible eth -m shell -f 10 -T 1 -a "geth --password ./Documents/password account new"``

  - 列出所创建的账户：
  ``ansible eth -m shell -f 10 -T 1 -a "geth account list" | grep {.*} -o``

```text
主链节点地址：(172.18.196.[1-9])
ansible group: eth
{af15e7f68199916bb9006e3058532429bac3f1bb}
{2e1b75a95277595b8d4157bac9c5bdd3cce15c9b}
{380b47345e8a40fe1d3a91ab254969bed26c83ea}
{ce69fc4eb267f01099b557cad30dc2a6f65eda2d}
{0a8df52ee190b391affcaaf4781ecfeab4c10b7d}
{feca0679ad3661e099a32ef1308780bd17e18b2e}
{2c9191c65c6e52eb911fc8cc6d2fe6c6441e6e2b}
{f079f3e7bf10595f47a323ae25e33edb51041f73}
{53e745aa89ea1b9d3498969791765d9a3b9f922b} (172.18.196.1)
{b2b32f90bc34587e1c28388af1b72b2d3acaa09a}

{fa578b05fbd9e1e7c1e69d5add1113240d641bc2}(本机地址)

侧链节点地址：(172.18.196.[12-20])
ansible group: eth2
{a91e54d780f916c8f16c8ff817debf9a6cd98eb6}
{3c1d439ab04aa910259aa06c428d513d5231d5ee}
{cb21073a3bb17db3234eb86a061a26d7ec0acf8d}
{02b5c9eebc1016b1f32929b72471f50b57c09cc6}
{980469cf401238e6b1d333101a24cfad7736d708} (172.18.196.12)
{5970c83e6d2db8829c9e30a3c50c01da11de4292}
{4a77607817e7f1216338c00cf80560ed5893ace5}
{4cb3e9bea76c1e1e404cce65e85e6bc43eda9fff}
{dbe7454979d1545b2d7697297a82323fc2628a3a}
{878a4d315493b29ed3b6e1ad117a71931d724949}

```

- 启动节点：
``geth --rpc --rpcaddr "0.0.0.0" --rpccorsdomain "*" --networkid 666 --port "30303" --rpcapi "db,eth,net,web3" console``

 - 启动其他节点

``geth --rpc --rpccorsdomain "*" --networkid 666 --port "30303" --rpcapi "db,eth,net,web3" --bootnodes "enode://609d64bae0f25685d7a3d05597c2cd281ead4f2d48abe329f77049d0cbc8eeb06027f692720dd4eec0131d988919258efd51d8cdd6946e958d8c3382a6e27644@172.18.196.5:30303" console``

 - 后台运行

``nohup geth --rpc --rpccorsdomain "*" --networkid 666 --port "30303" --rpcapi "db,eth,net,web3" --bootnodes "enode://609d64bae0f25685d7a3d05597c2cd281ead4f2d48abe329f77049d0cbc8eeb06027f692720dd4eec0131d988919258efd51d8cdd6946e958d8c3382a6e27644@172.18.196.5:30303" &``

 - 本机启动

``geth --rpc --rpcaddr "0.0.0.0" --rpccorsdomain "*" --ws --wsorigins "http://localhost:3000" --networkid 444 --port "30303" --rpcapi "db,eth,net,web3" --bootnodes "enode://279c8f3d7e212d7b473acbe08dc8ecc6957adba54383a120f2bf60b20fb7d2f0891b5bca8ae90addddfdb028692290d87b9db893ef95694d5fb3c5ec06e83ef8@172.18.196.12:30303" console --unlock fa578b05fbd9e1e7c1e69d5add1113240d641bc2``

合约地址

- Masterchain
  - node:
    `494a1c22782e7dadb2abf7c67a5fe65a13c241e4c1103493215842f08e5a186eb2fa41eca9db37a5da3ece35fcdba9be5925854b5e35004aee6280d7ab1308d0@172.18.196.1:30303`

  - SNM:
	0x4225ddc38c57b0ef2debcdac8e87af05d9859940

  - MultiSigWallet:
    0xd27c47655a22f334ee0b40a11264bc3106a19232

  - SimpleGatekeeperWithLimitLive:
    0x5ae73123990580bbb0830de67d8f47210ede7dca

- SideChain
  - node:
    `279c8f3d7e212d7b473acbe08dc8ecc6957adba54383a120f2bf60b20fb7d2f0891b5bca8ae90addddfdb028692290d87b9db893ef95694d5fb3c5ec06e83ef8@172.18.196.12:30303`
  - Deployer:
    - `0xfa578b05fbd9e1e7c1e69d5add1113240d641bc2`(本机)
    - `0x980469cf401238e6b1d333101a24cfad7736d708`(172.18.196.12)


  - MultiSigWallet:
    0x4225ddc38c57b0ef2debcdac8e87af05d9859940
  - SNM:
    0xd27c47655a22f334ee0b40a11264bc3106a19232
  - SimpleGatekeeperWithLimit:
    0x5ae73123990580bbb0830de67d8f47210ede7dca
  - MultiSigWallet:
    0xc4c5fc9f9c4c78da9f6770e17410bf4e980dea12
  - MultiSigWallet:
    0x105e681becd1a37a6b5321e06d9c0b2d3fcf12bd
  - ProfileRegistry:
    0xc05298309ecec310c7944cb4afd48c8776f55c6c
  - Blacklist:
    0x8c5023477316aa9781d02adabcf63e12371e40cf
  - OracleUSD:
    0x1a4a8e6db68bcc3eb3bb820f35a979812fb2693b
  - Market:
    0x28f3fb59e79aff4962809cab78fab69ae8e95e3f
  - DeployList:
    0x3ab84e15533470a620826862a2affa7b12a3609d
  - AddressHashMap:
    0xc8fed8603e0e6bf0d9a6b6c9b89606135f60ed71

