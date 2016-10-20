#!/usr/bin/env bash

echo "Setting up mongodb and installing as a daemon"


sudo killall mongod || true
sudo rm -f /etc/init/mongodb.conf  # Remove annoying upstart daemon to install ours
sudo update-rc.d -f mongo_daemon remove
sudo ln -sfnv $CONFIG_DIR/etc/init.d/mongo_daemon /etc/init.d
sudo update-rc.d mongo_daemon defaults
sudo service mongo_daemon restart