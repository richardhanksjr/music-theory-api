#!/bin/bash

echo "Loading fixtures."
python /code/manage.py loaddata questions.json || exit 1