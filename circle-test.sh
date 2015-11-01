#!/bin/sh


VERSION=$1



docker run \
    -h django-app \
    --name django-app \
    -e BRANCH=`git rev-parse --abbrev-ref HEAD`  \
    -e DEPLOYMENT=development \
    -e TEST=1 \
    -e START_DELAY=10 \
    $HOST/$IMAGE:$VERSION
