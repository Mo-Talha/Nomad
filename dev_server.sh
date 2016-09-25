#!/usr/bin/env bash

function clean_up() {
  set +e
  kill 0
  exit
}

# Kill all child processes on script abort
trap clean_up SIGTERM SIGINT ERR

echo "Starting MongoDB"
mongod --config config/mongodb_dev.conf &

echo "Starting Redis"
redis-server config/redis_local.conf &

# Only exit on terminate or interrupt signal
while true; do
  sleep 1
done