#!/bin/bash
file=$1
[ -z "$file" ] && file=logs.txt
cut -d' ' -f1 $file | sort | uniq -c | sort -nr | head -n1 | awk '{print $1}'
