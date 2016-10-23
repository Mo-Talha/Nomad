SHELL=/bin/bash

install:
	@echo "*** Installing project dependencies. ***"
	@echo

	./install.sh

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

	@echo "Done"

clean:
	find . -name '*.pyc' -delete
	find . -name 'ghostdriver.log' -delete
	find . -name 'screenshot.png' -delete

clean_chunker: virtualenv
	find . -name '*.pickle' -delete

import_jobs: virtualenv
	@echo "*** Importing Jobmine data. This may take several hours. ***"
	@echo

	@echo "Importing jobs"
	PYTHONPATH=$(PYTHONPATH):. python data/main.py jobmine

	@echo
	@echo "*** Done ***"

import_comments: virtualenv
	@echo "*** Importing RateMyCoopJob data. This may take several hours or less. ***"
	@echo

	@echo "Importing comments"
	PYTHONPATH=$(PYTHONPATH):. python data/main.py ratemycoopjob

	@echo
	@echo "*** Done ***"


import: import_jobs import_comments

install_nltk_data: virtualenv
	@echo "*** Installing NLTK data. ***"
	@echo

	sudo python -m nltk.downloader -d /usr/local/share/nltk_data all

	@echo "Done"


train_compsci: virtualenv
	@echo "*** Training Computer Science Chunker. This may take a few minutes or less. ***"
	@echo

	PYTHONPATH=$(PYTHONPATH):. python data/analysis/train.py comp-sci

	@echo
	@echo "*** Done ***"

train: clean_chunker train_compsci

virtualenv:
	@if [[ "${VIRTUAL_ENV}" = "${HOME}/.virtualenv/Nomad" ]]; then \
		true; \
	else \
		source ~/.virtualenv/Nomad/bin/activate
	fi

export_data:
	mongodump --db nomad
