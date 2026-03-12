#!/bin/bash

echo "Создаем файлы..."

for i in {1..10}; do
    touch "test$i.txt"
    echo "Создан файл: test$i.txt"
done

echo "------------------------"
echo "Все файлы созданы. Удаляем в обратном порядке..."
echo "------------------------"

i=10
while [ $i -ge 1 ]; do
    if [ -f "test$i.txt" ]; then
        rm "test$i.txt"
        echo "Удален файл: test$i.txt"
    fi
    i=$((i - 1))
done

echo "------------------------"
echo "Готово! Все файлы удалены."
