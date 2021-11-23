FROM mysql:5.7

ENV MYSQL_ROOT_PASSWORD=123456

WORKDIR /home

ADD my.cnf /etc/mysql/mysql.conf.d/my.cnf
ADD . /home

EXPOSE 3306