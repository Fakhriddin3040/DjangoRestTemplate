#!/bin/sh

NGINX_CONF_ROOT="/etc/nginx/conf.d"
CERTBOT_DOMAIN_ROOT="/etc/letsencrypt/live/$DOMAIN_URL"

if [ -z "$CERTBOT_CONTAINER" ]; then
    echo "CERTBOT_CONTAINER: Certbot container name is required."
    exit 1
fi

if [ -z "$PROXY_CONTAINER" ]; then
    echo "PROXY_CONTAINER: Proxy container name is required."
    exit 1
fi

if ! docker ps -a --filter "name=$CERTBOT_CONTAINER" > /dev/null 2>&1; then
    echo "Error: Certbot container not found."
    exit 1
fi

if [ -f "$NGINX_CONF_ROOT/ssl.conf" ]; then
    echo "SSL configuration for NGINX found."
    echo "Turning ssl configuration off..."

    mv "$NGINX_CONF_ROOT/ssl.conf" "$NGINX_CONF_ROOT/ssl.conf.bak"

    echo "Restarting proxy container($PROXY_CONTAINER) for accepting certbot requests."
    docker compose restart "$PROXY_CONTAINER"
    echo "$PROXY_CONTAINER restarted."
else
    echo "SSL configuration for NGINX not found."
fi

if docker container ps -a --filter "name=$PROXY_CONTAINER" --filter "status=exited" --format="{{.Names}}"; then
    echo "Unexpected error occured, while healing $PROXY_CONTAINER."
    exit 1
fi

echo "Requesting new SSL certificate..."

docker compose up $CERTBOT_CONTAINER

if [ -f "$CERTBOT_DOMAIN_ROOT/fullchain.pem" ]; then
    echo "SSL certificate generated successfully."
    mv "$NGINX_CONF_ROOT/ssl.conf.bak" "$NGINX_CONF_ROOT/ssl.conf"

    echo "Restarting proxy container($PROXY_CONTAINER) for accepting new SSL configuration..."
    docker compose restart "$PROXY_CONTAINER"

    if docker ps -a --filter "name=$PROXY_CONTAINER" --filter "status=exited" --format="{{.Names}}"; then
        echo "Could not run $PROXY_CONTAINER. Unexpected error occured."
        exit 1
    fi
else
    echo "Certificate initialization compelted."
fi

exit 0