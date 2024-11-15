#!/bin/sh

NGINX_CONF_DIR="/etc/nginx/conf.d"
SSL_CONF="/ssl.conf"

# Проверяем наличие ssl.conf
if [ -f "$NGINX_CONF_DIR/ssl.conf" ]; then
    echo "Перемещаю $NGINX_CONF_DIR/ssl.conf в корень..."
    mv "$NGINX_CONF_DIR/ssl.conf" "$SSL_CONF"
fi

# Запуск certbot для генерации сертификатов
echo "Запускаю certbot..."
certbot certonly --webroot -w /var/www/certbot \
    --non-interactive \
    --email "$DOMAIN_EMAIL" \
    -d "$DOMAIN_URL" \
    --agree-tos


# Возвращаем ssl.conf, если он был перемещён
if [ ! -f "$NGINX_CONF_DIR/ssl.conf" ]; then
    echo "Возвращаю $SSL_CONF в $NGINX_CONF_DIR..."
    mv "$SSL_CONF" "$NGINX_CONF_DIR/ssl.conf"
else
    echo "$NGINX_CONF_DIR/ssl.conf уже существует"
fi

echo "Скрипт завершён успешно."
