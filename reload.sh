#!/bin/bash
set -e

echo "Restating Docker container..."
echo "Tearing down existing container..."
docker-compose down

echo "Building Docker container and starting in daemon mode"
docker-compose up --build -d

echo "Building JavaScript assets"
./js.sh

echo "Loading questions into database:"
docker-compose exec web python manage.py loaddata questions.json


echo "Docker successfully restarted"
