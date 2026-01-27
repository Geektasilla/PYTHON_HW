#!/bin/bash

SOURCE="/opt/101025-ptm/viktoria_mariella/input"
DEST="/opt/101025-ptm/viktoria_mariella/sorted"

# Проверяем, что исходная директория существует
if [ ! -d "$SOURCE" ]; then
    echo "Ошибка: Исходная директория не найдена."
    exit 1
fi

for file_path in "$SOURCE"/*
do
    # Получаем имя файла без пути к нему
    filename=$(basename "$file_path")

    # Выполняем проверку, является ли имя числом и делится ли оно на 2 без остатка
    if (( filename % 2 == 0 )); then
        mv "$file_path" "$DEST/"
    fi
done

echo "Файлы успешно перенесены."
