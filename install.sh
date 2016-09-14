#!/usr/bin/env bash

install_git(){
    # Get latest version of git
    if ! ls /etc/apt/sources.list.d/ 2>&1 | grep -q git-core-ubuntu-ppa; then
        sudo add-apt-repository -y ppa:git-core/ppa
    fi

    sudo apt-get update -qq -y
    sudo apt-get install -y git

}

install_mongodb(){
    if ! ls /etc/apt/sources.list.d/ 2>&1 | grep -q mongodb.list; then
        # Import mongodb public GPG key
        sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927

        echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list

        sudo apt-get update -qq -y
        sudo apt-get install mongodb-org

        # Stop MongoDB
        sudo service mongod stop
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

# Get password
sudo echo

install_git
install_mongodb
install_phantom