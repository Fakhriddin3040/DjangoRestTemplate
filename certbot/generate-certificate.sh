#!/bin/sh

# Убедитесь, что предыдущие сертификаты удалены
rm -rf /etc/letsencrypt/live/certfolder*

certbot certonly --standalone \
    --webroot -w /var/www/certbot \
    --non-interactive \
    --email $DOMAIN_EMAIL \
    -d $DOMAIN_URL \
    --agree-tos

# Проверка успешности получения сертификатов
if [ -f /etc/letsencrypt/live/certfolder/fullchain.pem ] && [ -f /etc/letsencrypt/live/certfolder/privkey.pem ]; then
    echo "Сертификаты были успешно сгенерированы."
else
    echo "Сертификаты не были сгенерированы. Проверьте настройки."
fi
