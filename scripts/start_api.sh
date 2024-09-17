#! /bin/bash

# This script is used to start the API.

#ensure that $PROJECT_DIR is set

export PROJECT_DIR=$(pwd)

if [ -z "$PROJECT_DIR" ]; then
    echo "PROJECT_DIR is not set. Please set this variable to the root directory of the project."
    exit 1
fi

python3 manage.py runserver 127.0.0.1:$DJANGO_PORT
