#!/bin/sh
sleep $START_DELAY


# For docker-compose usage
: ${POSTGRES_SERVICE_HOST:=$POSTGRES_PORT_5432_TCP_ADDR}
: ${POSTGRES_SERVICE_PORT:=$POSTGRES_PORT_5432_TCP_PORT}
: ${DEPLOYMENT:=development}
export POSTGRES_SERVICE_HOST
export POSTGRES_SERVICE_PORT

python3 manage.py migrate

echo Ran migrations

if [ "$DEPLOYMENT" = "production" ]; then
    echo Run production system
    /usr/bin/supervisord --nodaemon -c /etc/supervisor/supervisord.conf
else
    echo Running python development server
    python3 manage.py runserver
fi

if [ "$TEST" = 1 ]; then
    echo Run tests
    ./run_tests.sh
fi
