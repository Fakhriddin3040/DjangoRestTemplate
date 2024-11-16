#!/bin/sh

# Установить необходимые пакеты
apk add --no-cache bash dcron

# Проверить доступ к Docker
docker ps > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Docker socket недоступен!"
    exit 1
fi

# Запустить cron
crond

# Запустить планировщик
sh /scripts/certbot_schedule.sh

# Подождать 10 секунд
sleep 10

# Перезапустить NGINX
echo "Перезапускаем прокси сервер"

docker container ps --filter "name=proxy" --format="{{.Names}}"

# Удерживать контейнер активным
tail -f /dev/null
