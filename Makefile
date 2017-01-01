SHELL=/bin/bash

install:
	@echo "*** Installing project dependencies. ***"
	@echo

	./install.sh

	@echo "*** Installing NLTK data ***"
	@echo
	sudo cp -a nltk_data /usr/local/share/nltk_data
	@echo

	@echo "Done"

devel:
	@echo "*** Setting development environment. ***"
	@echo

	./setup.sh dev

	@echo "Done"

prod:
	@echo "*** Setting production environment. ***"
	@echo

	./setup.sh prod

	npm run build

	@echo "Done"

test:
	source ~/.virtualenv/Nomad/bin/activate && PYTHONPATH=$(PYTHONPATH):. python -m unittest discover --pattern=*test.py -v

clean:
	find . -name '*.pyc' -delete
	find . -name 'ghostdriver.log' -delete
	find . -name 'screenshot.png' -delete

clean_chunker:
	find . -name '*.pickle' -delete

import_jobs:
	@echo "*** Importing WaterlooWorks data. This may take several hours. ***"
	@echo

	@echo "Importing jobs"
	source ~/.virtualenv/Nomad/bin/activate && PYTHONPATH=$(PYTHONPATH):. python data/main.py waterlooworks

	@echo
	@echo "*** Done ***"

import_comments:
	@echo "*** Importing RateMyCoopJob data. This may take several hours or less. ***"
	@echo

	@echo "Importing comments"
	source ~/.virtualenv/Nomad/bin/activate && PYTHONPATH=$(PYTHONPATH):. python data/main.py ratemycoopjob

	@echo
	@echo "*** Done ***"

import_locations:
	@echo "*** Installing Geonames data ***"
	@echo
	mongoimport -d nomad -c locations --type tsv --file location_data/allCountries.txt --fields countrycode,postalcode,name,name1,code1,name2,code2,name3,code3,latitude,longitude,accuracy
	@echo

import: import_jobs import_comments

train_compsci:
	@echo "*** Training Computer Science Chunker. This may take a few minutes or less. ***"
	@echo

	source ~/.virtualenv/Nomad/bin/activate && PYTHONPATH=$(PYTHONPATH):. python data/analysis/train.py comp-sci

	@echo
	@echo "*** Done ***"

train: clean_chunker train_compsci

index:
	@echo "*** Indexing Elasticsearch. This may take a few minutes or less. ***"
	@echo

	@echo "Indexing"
	source ~/.virtualenv/Nomad/bin/activate && PYTHONPATH=$(PYTHONPATH):. python data/search/elastic.py

	@echo
	@echo "*** Done ***"

export_data:
	mongodump --db nomad