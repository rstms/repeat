# top-level Makefile 

# remove module from the local python environment
uninstall:
	pip uninstall -y $(project)

# install to the local environment from the source directory
install:
	pip install --use-feature=in-tree-build --upgrade .

# local install in editable mode for development
devinstall: uninstall build
	pip install --use-feature=in-tree-build --upgrade -e .[dev]

# delete temporary development files
clean: 
	rm -rf .pytest_cache
	rm -rf ./build
	find . -type d -name __pycache__ | xargs -r rm -rf
	find . -type d -name \*.egg-info | xargs -r rm -rf
	find . -type f -name \*.pyc | xargs -r rm
	for clean in $(call included,clean); do ${MAKE} $$clean; done

include $(wildcard make.include/*.mk)
