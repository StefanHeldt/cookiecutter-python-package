#!make
.PHONY: clean

##############################
# GLOBALS
##############################
PROJECT_NAME=template_python_package

SHELL:=/bin/bash
VENV_ROOT=.venv
VENV_BIN=$(VENV_ROOT)/BIN

##############################
# COMMANDS
##############################

# Install package
dev: precommit
	@echo "Installing package..." \
	pip install --upgrade poetry; \
	poetry install;
	
# Setup development environment for project
precommit: venv
	@echo "Setting up development environment..." \
	source $(VENV_BIN)/activate; \
	pip3 install pre-commit; \
	pre-commit install -t pre-commit; \
	pre-commit install -t pre-push; \
	pre-commit autoupdate;

# Setup virtual environment
venv:
	@echo "Creating virtual environment..." \
	pip3 install virtualenv --user; \
	virtualenv $(VENV_ROOT);

##############################
# Cleaning
##############################

clean:		# WARNING removes data from directory
	@echo
	@echo "\nRemoving all data from local directory..."
	rm -rf data/*; \
	rm -rf logs/*; \
	rm -rf reports/*