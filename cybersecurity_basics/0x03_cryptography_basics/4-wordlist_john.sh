#!/bin/bash
john --wordlist=/usr/share/wordlists/rockyou.txt --config=/dev/null --pot=4-password.txt --format=raw-sha256 "$1"
