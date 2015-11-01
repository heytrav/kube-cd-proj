#!/bin/sh


VERSION=$1



docker run \
    -h django-app \
    --name django-app \
    -e BRANCH=`git rev-parse --abbrev-ref HEAD`  \
    -e DEPLOYMENT=development \
    -e DBNAME=circle_test \
    -e POSTGRES_USER=ubuntu \
    -e POSTGRES_SERVICE_HOST=0.0.0.0 \
    -e POSTGRES_SERVICE_PORT=5432 \
    -e TEST=1 \
    $HOST/$IMAGE:$VERSION
