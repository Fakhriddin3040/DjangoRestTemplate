#!/bin/sh

# Установить необходимые пакеты
apk add --no-cache bash dcron

# Запустить cron
crond

# Запустить планировщик
/bin/bash /scripts/certbot_schedule.sh

# Удерживать контейнер активным
tail -f /dev/null