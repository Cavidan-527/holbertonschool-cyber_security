#!/bin/bash
file=$1
[ -z "$file" ] && file=logs.txt
ip=$(cut -d' ' -f1 $file | sort | uniq -c | sort -nr | head -n1 | awk '{print $2}')
grep "^$ip " $file | awk -F\" '{print $6}' | sort | uniq -c | sort -nr | head -n1 | awk '{$1=""; sub(/^ /,""); print}'
