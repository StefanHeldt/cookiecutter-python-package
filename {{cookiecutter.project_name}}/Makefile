#!make
.PHONY: clean

##############################
# GLOBALS
##############################
PROJECT_NAME={{cookiecutter.package_name}}

SHELL:=/bin/bash
VENV_ROOT=.venv
VENV_BIN=$(VENV_ROOT)/BIN

##############################
# COMMANDS
##############################

# Install package
dev: precommit
	@echo "Installing package and dependencies..." \
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
	@echo "Removing all data, logs and reports from local directory..."
	rm -rf data/*; \
	rm -rf logs/*; \
	rm -rf reports/*
