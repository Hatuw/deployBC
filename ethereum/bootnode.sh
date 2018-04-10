#!/bin/bash
if [! -f bootnode.key]; then
	bootnode -genkey bootnode.key
if

pkill bootnode

nohup bootnode -nodekey=bootnode.key > bootnode.log &