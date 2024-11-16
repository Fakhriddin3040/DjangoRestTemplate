#!/bin/sh

if ! docker ps > /dev/null 2>&1; then
    echo "Error: Docker socket not available."
    exit 1
else
    echo "Docker is available. Continue processes..."
fi

if docker container ps -a --filter "name=$PROXY_CONTAINER" --filter "status=exited" --format="{{.Names}}"; then
    echo "Container $PROXY_CONTAINER is not running."
    echo "Trying to up $PROXY_CONTAINER..."

    if [ -f /etc/nginx/conf.d/ssl.conf ] && \
        [ ! -f /etc/letsencrypt/live/$DOMAIN_URL/fullchain.pem ] && \
        docker container ps -a --filter "name=$PROXY_CONTAINER" --filter "status=exited" --format="{{.Names}}"; then

        echo "Found SSL configuration for $PROXY_CONTAINER(NGINX), but certificates were not found"
        echo "Requesting new certificatesr..."
        echo "Running ./scripts/certbot_init.sh..."

        /bin/bash ./scripts/certbot_request.sh
    fi
elif docker container ps -a --filter "name=$PROXY_CONTAINER" --format="{{.Names}}"; then
    echo "Container $PROXY_CONTAINER is running. Checking for ssl configurations"

    if [ ! -f /etc/nginx/conf.d/ssl.conf ]; then
        echo "Error: Ssl configuration for proxy(NGINX) not found. Check the configurations!"
        exit 1
    fi
fi

# Запустить cron
echo "Running cron..."
crond

# Запустить планировщик
if [ -f /app/scripts/certbot_schedule.sh ]; then
    echo "Running Certbot scheduler..."
    /bin/bash ./scripts/certbot_schedule.sh
else
    echo "Error: Scheduler script \
        ./scripts/certbot_schedule.sh not found."
    exit 1
fi

# Удерживать контейнер активным
echo "Holding container active."
tail -f /dev/null
