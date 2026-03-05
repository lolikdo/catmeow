#!/bin/bash

read -p "Введите массу (кг): " WEIGHT

read -p "Введите рост (в сантиметрах): " HEIGHT_CM

BMI=$(( WEIGHT * 10000 / (HEIGHT_CM * HEIGHT_CM) ))

echo "Ваш индекс массы тела (ИМТ): $BMI"
