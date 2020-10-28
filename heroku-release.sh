#!/bin/bash

python manage.py migrate
python manage.py createcachetable
python manage.py loaddata questions.json
npm run dev
python manage.py collectstatic --noinput
