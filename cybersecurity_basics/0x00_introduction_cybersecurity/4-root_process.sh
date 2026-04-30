#!/bin/bash
ps aux | grep "^$1" | grep -v -E " 0 +0 "
