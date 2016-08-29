DOCKER_IMAGE ?= ankoh/logbot:latest

image:
	docker build -t $(DOCKER_IMAGE) -f Dockerfile .

install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

tests:
	python3 tester.py

coverage:
	coverage run --source=bot tester.py
	coverage report

.PHONY: install freeze tests
