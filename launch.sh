#!/bin/sh


# For docker-compose usage
sleep $START_DELAY
: ${DEPLOYMENT:=development}

# run migrations
python3.5 manage.py migrate

if [ "$TEST" = 1 ]; then
    python3.5 manage.py test polls cookbook
    autopep8 --in-place --aggressive -r kube_cd_project/ polls/ cookbook/
else
    if [ "$DEPLOYMENT" = "production" ]; then
        echo Run wsgi server
        /usr/bin/supervisord --nodaemon -c /etc/supervisor/supervisord.conf
    else
        echo Running python development server
        python3.5 manage.py runserver 0.0.0.0:8000
    fi
fi
