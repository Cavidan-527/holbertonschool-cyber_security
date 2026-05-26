#!/bin/bash
john --show "$1" | head -n -2 | cut -d: -f2 > 4-password.txt $(john --wordlist=/usr/share/wordlists/rockyou.txt "$1" >/dev/null 2>&1)
