#!/bin/bash
curl -s https://www.amfiindia.com/spages/NAVAll.txt -o NAVAll.txt
awk -F ';' 'NF > 4 && $1 ~ /^[0-9]+$/ { print $4 "\t" $5 }' NAVAll.txt > schemes.tsv
echo "Extracted Scheme Name and Asset Value to schemes.tsv"
