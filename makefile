# FMAP
# A audio file format that takes in frequency values or notes and turns them into WAV format.
# GitHub: https://www.gitub.com/lewisevans2007/FMAP
# Licence: GNU General Public Licence v3.0
# By: Lewis Evans

python = python3
pip = pip3

all: dependencies_check build

install_all_and_build: install_requirements build

build:
	$(python) setup.py sdist bdist_wheel

dependencies_check:
	$(python) tools/dependencies_check.py

install_requirements:
	$(pip) install --upgrade pip
	$(pip) install -r requirements.txt
	$(pip) install --user --upgrade setuptools

clean:
	rm -rf build dist FMAP.egg-info

.PHONY: all build update_pip install_requirements clean