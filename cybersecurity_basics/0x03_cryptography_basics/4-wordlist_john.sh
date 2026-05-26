#!/bin/bash
john --wordlist=/usr/share/wordlists/rockyou.txt --pot=4-password.txt "$1"
