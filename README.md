# DeployBC

This project is used to deploy some blockchain(ethereum, hyperledger.ect)


## ethereum


## golem


## hyperledger

使用docker-py clent查看container的信息，其中一个结果示例如下：
``` json
{
    "networks": {
        "eth0": {
            "tx_errors": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "rx_bytes": 74262,
            "rx_packets": 544,
            "rx_dropped": 0,
            "tx_bytes": 19426,
            "tx_packets": 269
        }
    },
    "memory_stats": {
        "stats": {
            "active_anon": 2932736,
            "hierarchical_memory_limit": 2147483648,
            "inactive_file": 0,
            "total_pgpgout": 163,
            "total_active_anon": 2932736,
            "total_pgfault": 1228,
            "total_rss": 2932736,
            "total_pgmajfault": 0,
            "cache": 0,
            "mapped_file": 0,
            "pgmajfault": 0,
            "total_pgpgin": 879,
            "rss": 2932736,
            "total_writeback": 0,
            "pgpgin": 879,
            "writeback": 0,
            "total_unevictable": 0,
            "total_mapped_file": 0,
            "rss_huge": 0,
            "active_file": 0,
            "total_inactive_anon": 0,
            "total_active_file": 0,
            "pgpgout": 163,
            "total_cache": 0,
            "unevictable": 0,
            "total_inactive_file": 0,
            "total_dirty": 0,
            "pgfault": 1228,
            "total_rss_huge": 0,
            "dirty": 0,
            "inactive_anon": 0
        },
        "limit": 2147483648,
        "max_usage": 3883008,
        "usage": 3309568
    },
    "precpu_stats": {
        "cpu_usage": {
            "usage_in_usermode": 20000000,
            "total_usage": 70547379,
            "usage_in_kernelmode": 30000000,
            "percpu_usage": [
                7455995,
                9139592,
                5870049,
                6142919,
                28076587,
                4996681,
                3064883,
                5800673
            ]
        },
        "throttling_data": {
            "periods": 0,
            "throttled_time": 0,
            "throttled_periods": 0
        },
        "system_cpu_usage": 9772153930000000
    },
    "pids_stats": {
        "current": 8
    },
    "num_procs": 0,
    "storage_stats": {},
    "cpu_stats": {
        "cpu_usage": {
            "usage_in_usermode": 20000000,
            "total_usage": 70547379,
            "usage_in_kernelmode": 30000000,
            "percpu_usage": [
                7455995,
                9139592,
                5870049,
                6142919,
                28076587,
                4996681,
                3064883,
                5800673
            ]
        },
        "throttling_data": {
            "periods": 0,
            "throttled_time": 0,
            "throttled_periods": 0
        },
        "system_cpu_usage": 9772161860000000
    },
    "preread": "2018-05-07T10:57:05.577975746Z",
    "read": "2018-05-07T10:57:06.578186056Z",
    "id": "ab807f258f0cf60819465e0db31be33af4b4be25ebb38507afb046ac0179cd27",
    "blkio_stats": {
        "io_service_bytes_recursive": [],
        "sectors_recursive": [],
        "io_service_time_recursive": [],
        "io_wait_time_recursive": [],
        "io_merged_recursive": [],
        "io_time_recursive": [],
        "io_serviced_recursive": [],
        "io_queue_recursive": []
    },
    "name": "/dev-peer1.org2.example.com-mycc-1.0"
}
```


### Reference
- [hyperledger](http://hyperledger-fabric.readthedocs.io/en/release-1.1)
- [caliper](https://github.com/hyperledger/caliper)
- [docker-py 文档](https://docker-py.readthedocs.io/en/latest/containers.html)
