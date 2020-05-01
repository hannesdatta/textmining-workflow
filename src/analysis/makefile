# Makefile
# requires GNUMake32
# Installation instructions: http://tilburgsciencehub.com/setup


analyze: ../../gen/analysis/output/analysis.html

../../gen/analysis/temp/preclean.csv: preclean.R ../../gen/data-preparation/output/dataset.csv
	R --vanilla --args "" < "preclean.R"


../../gen/analysis/output/analysis.html: analysis.Rmd ../../gen/analysis/temp/preclean.csv
	R -e "rmarkdown::render('analysis.Rmd', output_file = '../../gen/analysis/output/analysis.html')"

wipe:
	python wipe.py