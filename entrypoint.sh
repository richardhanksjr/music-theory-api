#!/bin/bash

echo "Loading fixtures."
python3 /code/manage.py loaddata questions.json || exit 1