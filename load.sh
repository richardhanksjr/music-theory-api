#!/bin/bash
set -e

echo "Restating Docker container..."
echo "Tearing down existing container..."
docker-compose down --remove-orphans

echo "Removing database volume..."
docker volume rm music-theory-api_postgres_data

echo "Building Docker container and starting in daemon mode..."
docker-compose up --build  -d

echo "Migrating database and creating cache table..."
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createcachetable

echo "Resetting fixtures, loading questions, and creating default users..."
docker-compose exec web python manage.py docker_sync

echo "Docker successfully restarted"