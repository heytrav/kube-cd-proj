FROM us.gcr.io/sample-application-1112/wiley:latest

MAINTAINER Travis Holton <wtholton@gmail.com>

ADD supervisor /etc/supervisor/

ADD requirements.txt /tmp/
RUN pip3 install -I -r /tmp/requirements.txt

WORKDIR /usr/local/kube_cd_project
ADD . /usr/local/kube_cd_project
RUN apt-get purge -y git && apt-get clean

ENTRYPOINT ["./launch.sh"]
