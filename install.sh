#!/usr/bin/env bash

set -e

install_packages(){
    # Get latest version of git
    if ! ls /etc/apt/sources.list.d/ 2>&1 | grep -q git-core-ppa; then
        sudo add-apt-repository -y ppa:git-core/ppa
        update_repo=yes
    fi

    # If we added new repositories
    if [ -n "$update_repo" ]; then
        sudo apt-get update -qq -y
    fi

    sudo apt-get install -y git

}

install_phantom(){
    if ! which phantomjs >/dev/null; then
        (
            cd /usr/local/share

            arch=$(uname -m)

            if ! [ $(arch) = "x86_64" ]; then
                arch="i686"
            fi

            wget "https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-${arch}.tar.bz2" -O- | sudo tar xfj -

            sudo ln -snf /usr/local/share/phantomjs-2.1.1-linux-${arch}/bin/phantomjs /usr/local/bin/phantomjs
        )
    fi
}

# Get password
sudo echo

install_packages
install_phantom