# FMAP
# A audio file format that takes in frequency values or notes and turns them into WAV format.
# GitHub: https://www.gitub.com/0x4248/FMAP
# Licence: GNU General Public Licence v3.0
# By: 0x4248

PYTHON = python3
PIP = pip3

ifeq (, $(shell which $(PYTHON)))
$(error "No $(PYTHON) in PATH, please install $(PYTHON) or set the PYTHON variable to the correct path")
endif

all: dependencies_check build

install_all_and_build: install_requirements build

build:
	$(PYTHON) setup.py sdist bdist_wheel

dependencies_check:
	$(PYTHON) tools/dependencies_check.py

install_requirements:
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	$(PIP) install --user --upgrade setuptools

clean:
	@echo "RM\tbuild dist FMAP.egg-info"
	@rm -rf build dist FMAP.egg-info

test:
	python -m FMAP test.FMAP test.wav

help:
	@echo "FMAP Makefile help"
	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo "  all:					Checks for requirements and builds"
	@echo "  build:					Builds package"
	@echo "  dependencies_check:	Checks for requirements"
	@echo "  clean:					Removes all build files"
	@echo "  test:					Tests for installed "
	@echo "  help:					Prints this help message"

.PHONY: all build update_pip install_requirements clean