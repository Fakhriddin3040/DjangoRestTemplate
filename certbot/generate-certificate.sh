#!/bin/sh

# Убедитесь, что предыдущие сертификаты удалены
rm -rf /etc/letsencrypt/live/certfolder*

# Запустите certbot с опцией --non-interactive
certbot certonly --standalone \
    --webroot-path /var/www/certbot \
    --non-interactive \
    --email $DOMAIN_EMAIL \
    -d $DOMAIN_URL \
    --cert-name=certfolder \
    --key-type rsa \
    --agree-tos

# Проверка успешности получения сертификатов
if [ -f /etc/letsencrypt/live/certfolder/fullchain.pem ] && [ -f /etc/letsencrypt/live/certfolder/privkey.pem ]; then
    # Копируем сертификаты в папку Nginx
    cp /etc/letsencrypt/live/certfolder/fullchain.pem /etc/nginx/cert.pem
    cp /etc/letsencrypt/live/certfolder/privkey.pem /etc/nginx/key.pem
else
    echo "Сертификаты не были сгенерированы. Проверьте настройки."
fi
