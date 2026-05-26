#!/bin/bash
john --wordlist=/usr/share/wordlists/rockyou.txt --pot="4-password.txt" --format=raw-sha256 "$1"
