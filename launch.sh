#!/bin/sh
sleep $START_DELAY


# For docker-compose usage
: ${DEPLOYMENT:=development}

python3.5 manage.py migrate

if [ "$TEST" = 1 ]; then
    echo Run tests
    ./run_tests.sh
else
    if [ "$DEPLOYMENT" = "production" ]; then
        echo Run wsgi server
        /usr/bin/supervisord --nodaemon -c /etc/supervisor/supervisord.conf
    else
        echo Running python development server
        python3.5 manage.py runserver 0.0.0.0:8000
    fi
fi
