#!/bin/bash
set -e

echo "Restating Docker container..."
echo "Tearing down existing container..."
docker-compose down --remove-orphans

echo "Building Docker container and starting in daemon mode"
docker-compose up --build  -d
docker-compose exec web python manage.py migrate

echo "Loading questions into database:"
docker-compose exec web python manage.py docker_sync


echo "Docker successfully restarted"
