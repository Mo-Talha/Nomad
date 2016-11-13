#!/usr/bin/env bash

# Stop old travis Mongo
sudo service mongodb stop
sudo killall mongod 2>/dev/null
sudo killall mongodb 2>/dev/null

# Remove old mongo packages
sudo apt-get purge mongodb mongodb-clients mongodb-server mongodb-dev
sudo apt-get purge mongodb-10gen
sudo apt-get autoremove

# Import mongodb public GPG key
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927

echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list

sudo apt-get update -qq -y
sudo apt-get install -y mongodb-org

sudo service mongod stop

sudo rm -f /etc/mongod.conf
sudo cp ./config/mongodb_dev.conf /etc/mongod.conf

sudo /usr/bin/mongod --fork --quiet --config /etc/mongod.conf

mongoimport -d nomad -c locations --type tsv --file location_data/allCountries.txt --fields countrycode,postalcode,name,name1,code1,name2,code2,name3,code3,latitude,longitude,accuracy