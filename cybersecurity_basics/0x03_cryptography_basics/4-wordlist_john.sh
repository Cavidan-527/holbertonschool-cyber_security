#!/bin/bash
xargs -a "$1" -I {} john --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-sha256 --pot=4-password.txt "$1"
