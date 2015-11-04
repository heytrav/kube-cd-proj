FROM ubuntu:15.10
MAINTAINER Travis Holton <wtholton@gmail.com>

RUN apt-get update && apt-get install -y git \
    python3.5 \
    python3.5-dev \
    python3.5-psycopg2 \
    python3-pip \
    libpq-dev \
    supervisor \
    postgresql
ADD supervisor /etc/supervisor/

ADD requirements.txt /tmp/
RUN pip3.5 install -I -r /tmp/requirements.txt

WORKDIR /usr/local/kube_cd_project
ADD . /usr/local/kube_cd_project
RUN apt-get purge -y git && apt-get clean

ENTRYPOINT ["./launch.sh"]
