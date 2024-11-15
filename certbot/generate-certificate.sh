#!/bin/sh

NGINX_CONF_DIR=/etc/nginx/conf.d

if [ -f $NGINX_CONF_DIR/ssl.conf ]; then
    mv $NGINX_CONF_DIR/ssl.conf /
    moved=true
fi

certbot certonly --webroot -w /var/www/certbot \
    --non-interactive \
    --email $DOMAIN_EMAIL \
    -d $DOMAIN_URL \
    --agree-tos

if [ $? -ne 0 ]; then
    echo "Failed to generate certificate"
    exit 1
fi

if [ "$moved" = true ]; then
    mv /ssl.conf $NGINX_CONF_DIR
fi