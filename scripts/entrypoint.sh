#!/bin/sh

# Установить необходимые пакеты
apk add --no-cache bash dcron

if ! docker ps > /dev/null 2>&1; then
    echo "Error: Docker socket not available."
    exit 1
else
    echo "Docker is available. Continue processes."
fi

# Запустить cron
echo "Running cron..."
crond

# Запустить планировщик
if [ -f /scripts/certbot_schedule.sh ]; then
    echo "Running Certbot scheduler..."
    sh /scripts/certbot_schedule.sh
else
    echo "Error: Scheduler script \
        /scripts/certbot_schedule.sh not found."
fi

# Подождать 10 секунд
echo "Waiting 10 seconds..."
sleep 10

# Перезапустить NGINX
echo "Restarting proxy server(NGINX)..."
proxy_container=$(docker container ps --filter "name=proxy" --format="{{.Names}}")

if [ -n "$proxy_container" ]; then
    docker restart "$proxy_container"
    echo "Proxy server ($proxy_container) successfuly restarted."
else
    echo "Error: Container service 'proxy' not found."
fi

# Удерживать контейнер активным
echo "Holding container active."
tail -f /dev/null
