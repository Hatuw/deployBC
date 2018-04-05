#!/bin/bash
# install necessary tools
sudo apt-get install git -y

git clone https://github.com/golemfactory/golem.git

sudo apt-get install -y openssl python3-dev libffi-dev pkg-config \
    libjpeg-dev libopenexr-dev libssl-dev autoconf libgmp-dev \
    libfreeimage-dev libtool python3-netifaces python3-psutil \
    python3-pip docker.io

# enable docker usage add user to docker group
sudo usermod -a -G docker $USER

# upgrade setuptools
pip3 install setuptools -U

# install Python libs
cd golem && pip3 install --user -r requirements.txt

# not finish yet.. =v=

