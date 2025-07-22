# Convert all notebooks and build site
all: convert serve

# Convert all notebooks in notebooks/ directory
convert:
	@for notebook in notebooks/*.ipynb; do \
		if [ -f "$$notebook" ]; then \
			python notebooks/convert_notebook.py "$$notebook"; \
		fi \
	done

# Build Hugo site
build:
	hugo

# Serve development site
serve: convert
	hugo server -D

# Clean generated files
clean:
	rm -rf public/
	rm -rf content/posts/*.md

.PHONY: all convert build serve clean