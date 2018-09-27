/etc/init.d/nginx start & uwsgi --socket /tmp/mysite.sock --module deliciousbody_api_server.wsgi --chmod-socket=666



