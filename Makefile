.PHONY: install test clear

NAME = test_env

SHELL := bash
python = python3

ifeq ($(OS),Windows_NT)
	python := python
endif

install:
	pip install $(pip_user_option) --upgrade pip \
	pip install $(pip_user_option) -r requirements.txt 

test:
	pytest -v -s test_hamming.py

clear:
	@rm -fr __pycache__ \
	@rm -fr .pytest_cache
