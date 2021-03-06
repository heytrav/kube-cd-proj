#!/bin/sh

set -e

# For docker-compose usage
: ${START_DELAY:=0}
sleep $START_DELAY
: ${DEPLOYMENT:=development}

# run migrations
python3.5 manage.py migrate

if [ "$TEST" = 1 ]; then
    python3.5 manage.py test polls cookbook
    autopep8 --in-place --aggressive -r kube_cd_project/ polls/ cookbook/
    if [ "$CIRCLE_TEST_REPORTS" != "" ]; then
        echo Copying coverage.xml to $CIRCLE_TEST_REPORTS
        cp coverage.xml $CIRCLE_TEST_REPORTS/
    fi
else
    if [ "$DEPLOYMENT" = "production" ]; then
        echo Run wsgi server
        /usr/bin/supervisord --nodaemon -c /etc/supervisor/supervisord.conf
    else
        echo Running python development server
        python3.5 manage.py runserver 0.0.0.0:8000
    fi
fi
