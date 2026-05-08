#!/bin/bash
egrep -v "^\s*#|^\s*$" /etc/ssh/sshd_config
