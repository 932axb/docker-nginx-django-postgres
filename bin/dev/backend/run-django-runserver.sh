#!/bin/bash

docker-compose -f docker-compose-dev.yml run backend python manage.py runserver 0.0.0.0:8000;
