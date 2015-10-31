#!/bin/sh


python manage.py migrate

if [ "$DEPLOYMENT" = "production" ]; then
    /usr/bin/supervisord --nodaemon -c /etc/supervisor/supervisord.conf
else
    python manage.py runserver
fi

if [ "$TEST" = 1 ]; then
    ./run_tests.sh
fi
