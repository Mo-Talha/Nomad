#!/usr/bin/env bash

install_java(){
    if ! which java >/dev/null; then
        sudo apt-get install -y openjdk-8-jre
    fi
}

install_git(){
    # Get latest version of git
    if ! ls /etc/apt/sources.list.d/ 2>&1 | grep -q git-core-ubuntu-ppa; then
        sudo add-apt-repository -y ppa:git-core/ppa

        sudo apt-get update -qq -y
        sudo apt-get install -y git
    fi
}

install_nginx(){
    if ! ls /etc/apt/sources.list.d/ 2>&1 | grep -q nginx-ubuntu-stable; then
        sudo add-apt-repository -y ppa:nginx/stable

        sudo apt-get update
        sudo apt-get install -y nginx
    fi
}

install_mongodb(){
    if ! ls /etc/apt/sources.list.d/ 2>&1 | grep -q mongodb-org-3.2; then
        # Import mongodb public GPG key
        sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927

        echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list

        sudo apt-get update -qq -y
        sudo apt-get install -y mongodb-org

        # Stop MongoDB
        sudo service mongod stop
    fi
}

install_redis(){
    if ! which redis-server >/dev/null; then
        # Get latest version of Redis
        wget http://download.redis.io/releases/redis-3.2.4.tar.gz

        tar xzf redis-3.2.4.tar.gz

        cd redis-3.2.4
        sudo make install

        cd utils
        sudo ./install_server.sh

        cd ../..
        sudo rm -rf redis-3.2.4
        sudo rm -rf redis-3.2.4.tar.gz
    fi
}

install_phantom(){
    if ! which phantomjs >/dev/null; then
        cd /usr/local/share

        arch=$(uname -m)

        if ! [ $(arch) = "x86_64" ]; then
            arch="i686"
        fi

        wget "https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-${arch}.tar.bz2" -O- | sudo tar xfj -

        sudo ln -snf /usr/local/share/phantomjs-2.1.1-linux-${arch}/bin/phantomjs /usr/local/bin/phantomjs
    fi
}

install_nodejs(){
    if ! which node >/dev/null; then
        sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 68576280

        sudo apt-add-repository "deb https://deb.nodesource.com/node_6.x $(lsb_release -sc) main"

        sudo apt-get update -qq -y
        sudo apt-get install -y nodejs
    fi
}

# Get password
sudo echo

install_java
install_git
install_nginx
install_mongodb
install_redis
install_nodejs
install_phantom