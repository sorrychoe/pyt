.PHONY: install test clear

NAME = test_env

SHELL := bash
python = python3

ifeq ($(OS),Windows_NT)
	python := python
endif

ifdef user
	pip_user_option = --user
endif

install:
	$(python) -m pip install $(pip_user_option) --upgrade pip \
	$(python) -m pip install $(pip_user_option) -r requirements.txt 

test:
	$(python) -W ignore::DeprecationWarning -m pytest -v -s test_hamming.py

report:
	$(python) -W ignore::DeprecationWarning -m pytest -v -s test_hamming.py --html=report.html --self-contained-html

clear:
	@rm -fr __pycache__ \
	@rm -fr .pytest_cache \
	@rm -fr report.html
