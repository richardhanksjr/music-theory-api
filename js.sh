#!/bin/bash

docker-compose exec web npm install
docker-compose exec web npm run dev