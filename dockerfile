FROM ubuntu:18.04

MAINTAINER DEV-GO

RUN apt-get update -y && \
    apt-get install -y \
    nginx \
    python3-dev \
    python3-pip

RUN pip3 install django uwsgi

COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip3 install -r requirements.txt

WORKDIR ..
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm -rf /etc/nginx/sites-enabled/default
COPY mysite_nginx.conf /etc/nginx/sites-enabled/mysite_nginx.conf

COPY . /mysite/
WORKDIR /mysite/

RUN chmod +x /mysite/docker_start.sh # give permission
CMD /mysite/docker_start.sh

expose 80
