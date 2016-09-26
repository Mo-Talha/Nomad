SHELL=/bin/bash

install:
	./install.sh

devel:
	./dev_server.sh

prod:
	./prod_server.sh

pip:
	pip install -r requirements.txt

export_data:
	mongodump --db nomad

clean:
	find . -name '*.pyc' -delete