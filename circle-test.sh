#!/bin/sh


VERSION=$1

POSTGRES_HOST=$(cat /etc/hosts | cut -d " " -f 3)
docker run \
    -h django-app \
    --name django-app \
    -v $CIRCLE_TEST_REPORTS/django:/tmp/django \
    -e BRANCH=`git rev-parse --abbrev-ref HEAD`  \
    -e DEPLOYMENT=development \
    -e DBNAME=circle_test \
    -e SECRET_KEY="Woohoo look at my test key!" \
    -e POSTGRES_USER=ubuntu \
    -e POSTGRES_SERVICE_HOST=$POSTGRES_HOST \
    -e POSTGRES_SERVICE_PORT=5432 \
    -e CIRCLE_TEST_REPORTS=/tmp/django \
    -e TEST=1 \
    $HOST/$IMAGE:$VERSION
