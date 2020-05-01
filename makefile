all: analysis data-preparation

.PHONY: all data-preparation analysis

data-preparation:
	$(MAKE) -C src/data-preparation

analysis: data-preparation
	$(MAKE) -C src/analysis

wipe: 
	$(MAKE) wipe -C src/data-preparation
	$(MAKE) wipe -C src/analysis
