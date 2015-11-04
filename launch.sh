#!/bin/sh
sleep $START_DELAY


# For docker-compose usage
: ${DEPLOYMENT:=development}
: ${VERBOSITY:=1}

python3.5 manage.py migrate

echo Ran migrations


if [ "$TEST" = 1 ]; then
    echo Run tests
    ./run_tests.sh
else
    if [ "$DEPLOYMENT" = "production" ]; then
        echo Run production system
        /usr/bin/supervisord --nodaemon -c /etc/supervisor/supervisord.conf
    else
        echo Running python development server
        python3.5 manage.py runserver -v $VERBOSITY 0.0.0.0:8000
    fi
fi
