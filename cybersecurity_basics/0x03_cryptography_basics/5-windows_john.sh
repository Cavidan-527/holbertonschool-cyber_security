#!/bin/bash
john --wordlist=/usr/share/wordlists/rockyou.txt --format=nt --pot=5-password.txt "$1"
