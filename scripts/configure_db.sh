#! /bin/bash

# This script is used to configure the database.

cd $PROJECT_DIR

python3 manage.py makemigrations
python3 manage.py migrate
