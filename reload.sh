#!/bin/bash
set -e

echo "Restating Docker container..."
echo "Tearing down existing container..."
docker-compose down

echo "Building Docker container and starting in daemon mode"
docker-compose up --build -d

#echo "Building JavaScript assets"
#./js.sh

echo "Docker successfully restarted"
