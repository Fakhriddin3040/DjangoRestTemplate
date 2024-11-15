#!/bin/bash

if docker ps --filter "name=$NGINX_CONTAINER_NAME" \
    --format "{{.Names}}" \
    | grep -q "$NGINX_CONTAINER_NAME";
    then

    echo "Nginx container is running. Try to update ssl certificates"

    docker exec -it "$NGINX_CONTAINER_NAME" sh -c "certbot renew"
else
    echo "Nginx container is not running. Certificates not updated."
    exit 1