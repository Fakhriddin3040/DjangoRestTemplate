#!/bin/sh

# Проверка переменных окружения
for var in WORK_DIR DJANGO_PORT ENVIRONMENT; do
    eval "value=\$$var"
    if [ -z "$value" ]; then
        echo "Error: $var is not set"
        exit 1
    fi
done

cd "$WORK_DIR" || exit
echo "Moved to working directory $WORK_DIR"

# Сбор статики
python3 manage.py collectstatic --no-input || { echo "Collectstatic failed"; exit 1; }

# Создание миграций
python3 manage.py makemigrations || { echo "Makemigrations failed"; exit 1; }

# Применение миграций с проверкой на успешность
python3 manage.py migrate || { echo "Migration failed"; exit 1; }

# Запуск сервера daphne

if [ "$ENVIRONMENT" = "production" ]; then
  daphne src.config.asgi:application --port "$DJANGO_PORT" || { echo "Failed to start server"; exit 1; }
else
  python3 manage.py runserver 0.0.0.0:"$DJANGO_PORT" || { echo "Failed to start server"; exit 1; }
fi

echo "Server running on port $DJANGO_PORT"
