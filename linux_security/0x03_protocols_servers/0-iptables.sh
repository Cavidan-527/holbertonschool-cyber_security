#!/bin/bash
sudo iptables -L -n --line-numbers -s "$1"
