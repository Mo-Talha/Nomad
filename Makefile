SHELL=/bin/bash

install:
	@echo "*** Installing dependencies. ***"
	@echo

	./install.sh

	@echo "Installing Python dependencies"
	pip install -r requirements.txt

	@echo "Installing NPM dependencies"
	npm install

	@echo "Done"

install_nltk_data:
	@echo "*** Installing NLTK data. ***"
	@echo

	sudo python -m nltk.downloader -d /usr/local/share/nltk_data all

	@echo "Done"

devel:
	@echo "*** Setting development environment. ***"
	@echo

	@echo "Configuring Mongo"
	sudo cp -v ./config/mongodb_dev.conf /etc/mongod.conf

	@echo "Configuring Redis"
	sudo cp -v ./config/redis_dev.conf /etc/redis/redis.conf

	@echo "Starting Mongo"
	sudo service mongod start

	@echo "Starting Redis"
	sudo service redis-server start

	@echo "Done"

prod:
	@echo "*** Setting production environment. ***"
	@echo

	@echo "Configuring Mongo"
	sudo cp -v ./config/mongodb_prod.conf /etc/mongod.conf

	@echo "Configuring Redis"
	sudo cp -v ./config/redis_prod.conf /etc/redis/redis.conf

	@echo "Starting Mongo"
	sudo service mongod start

	@echo "Starting Redis"
	sudo service redis-server start

	@echo "Done"

clean:
	find . -name '*.pyc' -delete
	find . -name 'ghostdriver.log' -delete
	find . -name 'screenshot.png' -delete

clean_chunker:
	find . -name '*.pickle' -delete

import_jobs:
	@echo "*** Importing Jobmine data. This may take several hours. ***"
	@echo

	@echo "Importing jobs"
	PYTHONPATH=$(PYTHONPATH):. python data/main.py jobmine

	@echo
	@echo "*** Done ***"

import_comments:
	@echo "*** Importing RateMyCoopJob data. This may take several hours or less. ***"
	@echo

	@echo "Importing comments"
	PYTHONPATH=$(PYTHONPATH):. python data/main.py ratemycoopjob

	@echo
	@echo "*** Done ***"


import: import_jobs import_comments

train_compsci:
	@echo "*** Training Computer Science Chunker. This may take a few minutes or less. ***"
	@echo

	PYTHONPATH=$(PYTHONPATH):. python data/analysis/train.py comp-sci

	@echo
	@echo "*** Done ***"

train: clean_chunker train_compsci

export_data:
	mongodump --db nomad
