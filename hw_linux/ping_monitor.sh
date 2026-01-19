#!/bin/bash

# Адрес по умолчанию - google.com, или то, что введет пользователь
TARGET=${1:-google.com}

echo "Запущен мониторинг $TARGET. Ожидание сбоев..."

FAIL_COUNT=0

while true; do
    # Отправляем 1 пакет, ждем максимум 2 секунды
    RESPONSE=$(ping -c 1 -t 2 "$TARGET" 2>&1)
    EXIT_CODE=$?

    if [ $EXIT_CODE -eq 0 ]; then
        FAIL_COUNT=0
        
        # Вытаскиваем время (проверено на вашем Mac)
        PING_TIME=$(echo "$RESPONSE" | sed -nE 's/.*time=([0-9.]+).*/\1/p')
        
        # Округляем до целого
        INT_TIME=${PING_TIME%.*}

        # Если время больше 100 мс - выводим предупреждение
        if [ -n "$INT_TIME" ] && [ "$INT_TIME" -gt 100 ]; then
             echo "[!] Высокая задержка: ${PING_TIME} ms"
        fi
        # Если меньше 100 мс - скрипт просто молчит (как и требовалось)

    else
        # Если пинг не прошел
        ((FAIL_COUNT++))

        # Если 3 неудачи подряд - бьем тревогу
        if [ $FAIL_COUNT -ge 3 ]; then
            echo "[!!!] Соединение потеряно: 3 неудачные попытки подряд"
            FAIL_COUNT=0
        fi
    fi

    sleep 1
done
