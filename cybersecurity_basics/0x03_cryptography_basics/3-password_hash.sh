#!/bin/bash
openssl dgst -sha512 -hmac "$(openssl rand -hex 8)" <<< -n "$1" > 3_hash.txt
