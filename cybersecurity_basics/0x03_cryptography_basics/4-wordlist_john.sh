#!/bin/bash
john --wordlist=/usr/share/wordlists/rockyou.txt $1 2>&1 | tee /dev/stderr | awk '/\(/{print $1}' > 4-password.txt
