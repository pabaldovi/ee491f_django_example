#!/bin/bash

# This script migrates the database

python manage.py makemigrations blog
python manage.py migrate