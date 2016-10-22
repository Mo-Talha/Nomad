#!/usr/bin/env bash

sudo echo

echo "Configuring MongoDB"

sudo killall mongod 2>/dev/null
sudo rm -f /etc/mongod.conf

sudo addgroup --quiet mongod 2>/dev/null
sudo adduser --quiet --system --no-create-home --ingroup redis --disabled-login --disabled-password mongod

sudo rm -f /etc/systemd/system/mongod.service
sudo rm -f /lib/systemd/system/mongod.service

echo "Configuring Redis"

sudo killall redis 2>/dev/null
sudo killall redis-server 2>/dev/null

sudo mkdir -p /etc/redis
sudo mkdir -p /var/log/redis
sudo mkdir -p /var/run/redis

sudo addgroup --quiet redis 2>/dev/null
sudo adduser --quiet --system --no-create-home --ingroup redis --disabled-login --disabled-password redis

sudo chown -R redis:redis /var/log/redis
sudo chown -R redis:redis /etc/redis
sudo chown -R redis:redis /var/run/redis

sudo rm -f /etc/redis/redis.conf
sudo rm -f /etc/redis/redis-server.conf
sudo rm -f /etc/init.d/redis-server
sudo rm -f /etc/systemd/system/redis-server.service
sudo rm -f /lib/systemd/system/redis-server.service

case "$1" in
    dev)
        sudo cp ./config/mongodb_dev.conf /etc/mongod.conf
        sudo cp ./config/redis_dev.conf /etc/redis/redis.conf
        ;;
    prod)
        sudo cp ./config/mongodb_prod.conf /etc/mongod.conf
        sudo cp ./config/redis_prod.conf /etc/redis/redis.conf
        ;;
esac

sudo cp ./server_setup/etc/systemd/system/mongod.service /etc/systemd/system/mongod.service
sudo cp ./server_setup/etc/systemd/system/redis-server.service /etc/systemd/system/redis-server.service

sudo chmod 755 /etc/systemd/system/mongod.service
sudo chmod 755 /etc/systemd/system/redis-server.service

sudo systemctl daemon-reload
