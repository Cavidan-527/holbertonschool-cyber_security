#!/bin/bash
ps -ef | grep "^$1" | grep -v -E " 0 +0 "
