#!/usr/bin/env bash

# Get password
sudo echo

echo "Configuring Mongo"
sudo cp -v ./config/mongodb_dev.yaml /etc/mongod.conf

echo "Configuring Redis"
sudo cp -v ./config/redis_dev.conf /etc/redis/redis.conf


echo "Starting Mongo"
sudo service mongod start

echo "Starting Redis"
sudo service redis-server start

echo "Done"
