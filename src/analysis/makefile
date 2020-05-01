# Makefile
# requires GNUMake32
# Installation instructions: http://tilburgsciencehub.com/setup


prep: ../../gen/data-preparation/output/dataset.csv

../../data/fortnite-rawdata.zip: download.py
	python download.py

../../gen/data-preparation/temp/unzipping.log: unzip.py ../../data/fortnite-rawdata.zip
	python unzip.py

../../gen/data-preparation/temp/parsed-data.csv: parse.py ../../gen/data-preparation/temp/unzipping.log
	python parse.py

../../gen/data-preparation/output/dataset.csv: textmining.py ../../gen/data-preparation/temp/parsed-data.csv
	python textmining.py

wipe:
	python wipe.py