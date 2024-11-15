#!/bin/sh

# Убедитесь, что предыдущие сертификаты удалены
rm -rf /etc/letsencrypt/live/certfolder*

certbot certonly --webroot -w /var/www/certbot \
    --non-interactive \
    --email $DOMAIN_EMAIL \
    -d $DOMAIN_URL \
    --agree-tos

# Проверка успешности получения сертификатов
if [ -f /etc/letsencrypt/live/astrotech-spaceapp.space/fullchain.pem ] then
    echo "Сертификаты были успешно сгенерированы."
else
    echo "Сертификаты не были сгенерированы. Проверьте настройки."
fi

