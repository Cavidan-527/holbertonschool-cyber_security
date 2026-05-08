#!/bin/bash
cat /etc/ssh/sshd_config | egrep -v '^\s*#|^\s*$'
