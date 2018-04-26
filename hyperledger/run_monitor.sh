#!/bin/bash

# create a InfluxDB container
docker run -d -p 8083:8083 -p 8086:8086 --expose 8090 --expose 8099 --name influxsrv -e PRE_CREATE_DB=cadvisor tutum/influxdb:latest

# create cAdvisor container and link to InfluxDB container
docker run --volume=/:/rootfs:ro --volume=/var/run:/var/run:rw --volume=/sys:/sys:ro --volume=/var/lib/docker:/var/lib/docker:ro --publish=8080:8080 --detach=true --link influxsrv:influxsrv --name=cadvisor google/cadvisor:latest -storage_driver=invluxdb -storage_driver_db=cadvisor -storage_driver_host=influxsrv:8086

# create Grafana container and lint to InfluxDB container
docker run -d -p 3000:3000 -e INFLUXDB_HOST=localhost -e INFLUXDB_PORT=8086 -e INFLUXDB_NAME=cadvisor -e INFLUXDB_USER=root -e INFLUXDB_PASS=root --link influxsrv:influxsrv --name grafana grafana/grafana:latest
