SHELL=/bin/bash

install:
	./install.sh

pip:
	pip install -r requirements.txt

export_data:
	mongodump --db nomad

export_data_to_dropbox:
	ssh rmc 'mongodump --db rmc'
	rsync -avz rmc:~/dump ~/Dropbox/Flow/db/
	( cd ~/Dropbox/Flow/db/ && zip -r dump.zip dump -x "**.DS_Store" )

clean:
	find . -name '*.pyc' -delete