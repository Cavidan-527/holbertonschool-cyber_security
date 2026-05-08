#!/bin/bash
grep -v "^\s*#" /etc/ssh/sshd_config | grep -v "^\s*$"
