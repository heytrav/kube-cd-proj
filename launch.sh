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
        DJANGO_COMMAND="gunicorn -b 0.0.0.0:8000 kube_cd_project.wsgi"
    else
        echo Running python development server
        DJANGO_COMMAND="python3.5 manage.py runserver 0.0.0.0:8000"
    fi
    sed -i 's/DJANGO_COMMAND/'"$DJANGO_COMMAND"'/g' /etc/supervisor/conf.d/django.conf
    /usr/bin/supervisord --nodaemon -c /etc/supervisor/supervisord.conf
fi
