#!/bin/bash

printf "%-15s %-7s %-7s %-7s %-7s\n" "Файл" "A" "T" "G" "C"
echo "----------------------------------------------------"

for file in *.fasta; do
    [ -e "$file" ] || continue
    
    if [ ! -s "$file" ]; then
        continue
    fi
    
    filename=$(basename "$file")
    
    sequence=$(grep -v "^>" "$file" | tr -d '\n' | tr -d ' ')
    
    count_A=$(echo "$sequence" | grep -o "A" | wc -l)
    count_T=$(echo "$sequence" | grep -o "T" | wc -l)
    count_G=$(echo "$sequence" | grep -o "G" | wc -l)
    count_C=$(echo "$sequence" | grep -o "C" | wc -l)
    
    # Если последовательность пустая, пропускаем
    if [ -z "$sequence" ]; then
        continue
    fi
    
    printf "%-15s %-7s %-7s %-7s %-7s\n" "$filename" "$count_A" "$count_T" "$count_G" "$count_C"
done

echo "----------------------------------------------------"
echo "Подсчет завершен."
