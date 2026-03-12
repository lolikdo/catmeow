#!/bin/bash
echo "Только имена:"
awk '{print $1}' students.txt
echo ""
echo "Только оценки:"
awk '{print $2}' students.txt
echo ""
echo "Номер строки и имя:"
awk '{print NR, $1}' students.txt
