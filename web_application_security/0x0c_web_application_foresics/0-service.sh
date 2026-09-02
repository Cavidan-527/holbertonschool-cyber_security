#!/bin/bash

grep -o 'pam_unix([^)]*)' auth.log | \
cut -d'(' -f2 | \
cut -d':' -f1 | \
sort | \
uniq -c | \
sort -nr
