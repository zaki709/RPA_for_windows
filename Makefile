VENV_DIR=.venv
SHELL=/bin/bash

.PHONY: init
init:
	python3 -m venv $(VENV_DIR)

.PHONY: install
install:
	pip install --upgrade pip && \
	pip install -r requirements.txt
	

.PHONY: run
run:
	$(VENV_DIR)/bin/python app/main.py
	