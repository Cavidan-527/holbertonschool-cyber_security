#!/bin/bash
grep "public" /etc/snmp/snmpd.conf | grep -v "^#"
