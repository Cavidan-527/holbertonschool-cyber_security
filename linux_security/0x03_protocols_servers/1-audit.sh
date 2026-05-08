#!/bin/bash
awk '!/^[ \t]*#/ && !/^[ \t]*$/' /etc/ssh/sshd_config
