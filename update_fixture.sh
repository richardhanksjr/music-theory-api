#!/bin/bash

docker-compose exec web python manage.py  dumpdata questions.Question questions.Tag --indent 4 --output questions/fixtures/questions.json