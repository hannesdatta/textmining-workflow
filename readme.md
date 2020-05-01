# Example of reproducible research workflow

This is a basic example repository using GNU Make, Python and R for a reproducible research workflow, as described in detail here: [tilburgsciencehub.com](http://tilburgsciencehub.com/).

The main aim of this to have a basic structure, which can be easily adjusted to use in an actual project.  In this example project, the following is done:
1. Download data in a zip file
2. Unzip data
3. Parse JSON data to CSV file
4. Load CSV file, and enrich textual data with text mining metrics using Python's TextBlob package for sentiment analysis
5. Present some descriptives and plots in R Markdown

## Dependencies
- Python via the Anaconda distribution
- TextBlob via `pip install -U textblob`
R
- R packages:
	install.packages("stargazer")
- Gnu make
- TeX distribution (I use TeX Live 2019)
- For the `makefile` to work, R, Gnu make and the TeX distribution (specifically `pdflatex`) need to be made available in the system path
- Detailed installation instructions can be found here: [tilburgsciencehub.com](http://tilburgsciencehub.com/)


## Notes
- `make clean` removes all unceessary temporary files.
- Tested under Linux Mint (should work in any linux distro, as well as on Windows and Mac)
- IMPORTANT: In `makefile`, when using `\` to split code into multiple lines, no space should follow `\`. Otherwise Gnu make aborts with error 193.
- Many possible improvements remain. Comments and contributions are welcome!
