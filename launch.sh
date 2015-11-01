#!/bin/sh
sleep $START_DELAY


# For docker-compose usage
: ${DEPLOYMENT:=development}
: ${VERBOSITY:=1}

python3 manage.py migrate

echo Ran migrations

if [ "$DEPLOYMENT" = "production" ]; then
    echo Run production system
    /usr/bin/supervisord --nodaemon -c /etc/supervisor/supervisord.conf
else
    echo Running python development server
    python3 manage.py runserver -v $VERBOSITY 0.0.0.0:8000
fi

if [ "$TEST" = 1 ]; then
    echo Run tests
    ./run_tests.sh
fi
