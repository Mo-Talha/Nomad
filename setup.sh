#!/usr/bin/env bash

sudo echo

ENV=$1

configure_virtualenv(){
    if [ ! -d "$HOME/.virtualenv" ]; then
        mkdir -p $HOME/.virtualenv
    fi

    virtualenv $HOME/.virtualenv/Nomad
}

configure_nginx(){
    sudo systemctl stop nginx 2>/dev/null
    sudo killall -9 nginx 2>/dev/null

    sudo rm -f /etc/nginx/sites-enabled/default
    sudo rm -f /etc/nginx/sites-available/default
    sudo rm -f /etc/nginx/sites-enabled/nomad
    sudo rm -f /etc/nginx/sites-available/nomad

    sudo cp ./server_setup/etc/nginx/sites-available/nomad /etc/nginx/sites-available/nomad
    sudo ln -sfnv /etc/nginx/sites-available/nomad /etc/nginx/sites-enabled/nomad

    sudo sed -i -e "s/<USER>/$USER/g" /etc/nginx/sites-available/nomad
}

configure_mongodb(){
    sudo killall mongod 2>/dev/null

    sudo rm -f /etc/mongod.conf

    sudo addgroup --quiet mongod 2>/dev/null
    sudo adduser --quiet --system --no-create-home --ingroup redis --disabled-login --disabled-password mongod

    sudo rm -f /etc/systemd/system/mongod.service
    sudo rm -f /lib/systemd/system/mongod.service

    case "$ENV" in
        dev)
            sudo cp ./config/mongodb_dev.conf /etc/mongod.conf
            ;;
        prod)
            sudo cp ./config/mongodb_prod.conf /etc/mongod.conf
            ;;
    esac

    sudo cp ./server_setup/etc/systemd/system/mongod.service /etc/systemd/system/mongod.service
}

configure_redis(){
    sudo killall redis 2>/dev/null
    sudo killall redis-server 2>/dev/null

    sudo rm -f /etc/redis/redis.conf
    sudo rm -f /etc/redis/redis-server.conf
    sudo rm -f /etc/init.d/redis-server
    sudo rm -f /etc/systemd/system/redis-server.service
    sudo rm -f /lib/systemd/system/redis-server.service

    sudo mkdir -p /etc/redis/
    sudo mkdir -p /var/log/redis/
    sudo mkdir -p /var/run/redis/

    sudo addgroup --quiet redis 2>/dev/null
    sudo adduser --quiet --system --no-create-home --ingroup redis --disabled-login --disabled-password redis

    sudo chown -R redis:redis /var/log/redis/
    sudo chown -R redis:redis /etc/redis/
    sudo chown -R redis:redis /var/run/redis/

    case "$ENV" in
    dev)
        sudo cp ./config/redis_dev.conf /etc/redis/redis.conf
        ;;
    prod)
        sudo cp ./config/redis_prod.conf /etc/redis/redis.conf
        ;;
    esac

    sudo cp ./server_setup/etc/systemd/system/redis-server.service /etc/systemd/system/redis-server.service
}

configure_uwsgi(){
    sudo systemctl stop nomad 2>/dev/null
    sudo killall -9 uwsgi 2>/dev/null

    sudo rm -f /tmp/uwsgi.ini
    sudo rm -f /tmp/nomad.sock
    sudo rm -f /tmp/nomad.pid
    sudo rm -f /etc/systemd/system/nomad.service

    sudo mkdir -p /var/log/uwsgi/
    sudo touch /var/log/uwsgi/uwsgi.log

    sudo cp ./config/uwsgi.ini /tmp/uwsgi.ini
    sudo sed -i -e "s/<USER>/$USER/g" /tmp/uwsgi.ini

    sudo chown -R www-data:www-data /tmp/uwsgi.ini
    sudo chown -R www-data:www-data /var/log/uwsgi/
    sudo setfacl -m u:www-data:rwx ~/Nomad/logs/

    sudo cp ./server_setup/etc/systemd/system/nomad.service /etc/systemd/system/nomad.service
    sudo sed -i -e "s/<USER>/$USER/g" /etc/systemd/system/nomad.service

    case "$ENV" in
    prod)
        sudo sed -i -e '$a\' /tmp/uwsgi.ini
        sudo /bin/bash -c  "echo 'env=ENV=prod' >> /tmp/uwsgi.ini"
        ;;
    esac
}

configure_elasticsearch(){
    sudo systemctl stop elasticsearch 2>/dev/null
    sudo killall elasticsearch 2>/dev/null

    sudo rm -f /etc/elasticsearch/elasticsearch.yml

    sudo addgroup --quiet elasticsearch 2>/dev/null
    sudo adduser --quiet --system --no-create-home --ingroup elasticsearch --disabled-login --disabled-password elasticsearch

    sudo mkdir -p /var/log/elasticsearch/
    sudo mkdir -p /etc/elasticsearch/

    sudo chown -R elasticsearch:elasticsearch /var/log/elasticsearch/
    sudo chown -R elasticsearch:elasticsearch /etc/elasticsearch/
    sudo chown -R elasticsearch:elasticsearch /var/lib/elasticsearch/
    sudo chown -R elasticsearch:elasticsearch /usr/share/elasticsearch

    sudo cp ./config/elasticsearch.yml /etc/elasticsearch/elasticsearch.yml
}

echo "Configuring Virtualenv"
configure_virtualenv

echo "Configuring Nginx"
configure_nginx

echo "Configuring MongoDB"
configure_mongodb

echo "Configuring Redis"
configure_redis

echo "Configuring uWSGI"
configure_uwsgi

echo "Configuring ElasticSearch"
configure_elasticsearch

sudo systemctl daemon-reload

echo "Starting MongoDB"
sudo systemctl start mongod

echo "Starting Redis"
sudo systemctl start redis-server

echo "Starting Virtualenv"
source $HOME/.virtualenv/Nomad/bin/activate

echo "Installing Python dependencies"
pip install -r requirements.txt

echo "Installing NPM dependencies"
npm install

echo "Installing Bower dependencies"
./node_modules/bower/bin/bower install

echo "Starting ElasticSearch"
sudo systemctl start elasticsearch

echo "Starting Nomad"
sudo systemctl start nomad

echo "Starting Nginx"
sudo systemctl start nginx
