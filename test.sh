#!/bin/bash
set -e

docker-compose exec web python manage.py test