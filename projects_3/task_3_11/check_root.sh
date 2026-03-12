#!/bin/bash

check_root() {
    if [ $EUID -ne 0 ]; then
        echo "Ошибка: Скрипт должен быть запущен от имени суперпользователя (root)."
        echo "Текущий UID: $EUID"
        exit 1
    fi
}

check_root

echo "Скрипт запущен от root. Продолжаем выполнение..."
echo "UID: $EUID"
