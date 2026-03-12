#!/bin/bash
echo "Студенты с оценкой выше 80:"
awk '$2 > 80' students.txt
echo ""
echo "Студенты с оценкой ниже 70:"
awk '$2 < 70' students.txt
echo ""
echo "Только первая строка:"
awk 'NR==1' students.txt
