#!/bin/bash
iptables -L -n --line-numbers | grep "$1"
