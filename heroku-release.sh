#!/bin/bash

python manage.py migrate
python manage.py createcachetable
python manage.py loaddata questions.json
