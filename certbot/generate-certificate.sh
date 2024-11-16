#!/bin/sh

NGINX_CONF_DIR="/etc/nginx/conf.d"

# Проверяем наличие ssl.conf
if [ -f "$NGINX_CONF_DIR/ssl.conf" ]; then
    echo "Перемещаем $NGINX_CONF_DIR/ssl.conf..."
    mv "$NGINX_CONF_DIR/ssl.conf" /
fi

# Запуск certbot для генерации сертификатов

certbot certonly --webroot -w /var/www/certbot \
    --non-interactive \
    --email "$DOMAIN_EMAIL" \
    -d "$DOMAIN_URL" \
    --agree-tos


# Возвращаем ssl.conf, если он был удалён
if [ ! -f "$NGINX_CONF_DIR/ssl.conf" ]; then
    echo "Возвращаем ssl.conf в $NGINX_CONF_DIR..."
    mv "/ssl.conf" "$NGINX_CONF_DIR/ssl.conf"
else
    echo "$NGINX_CONF_DIR/ssl.conf уже существует"
fi

echo "Скрипт завершён успешно."