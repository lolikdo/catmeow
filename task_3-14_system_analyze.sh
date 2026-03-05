#!/bin/bash
df -h | awk 'NR>1 {
    print $1, $5
    gsub(/%/,"",$5)
    if ($5 > 90) print "   ⚠️  ВНИМАНИЕ: " $1 " заполнен на " $5 "%"
}'
