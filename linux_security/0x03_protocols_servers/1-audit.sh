#!/bin/bash
awk '!/^[ \t]*#/ && NF' /etc/ssh/sshd_config
