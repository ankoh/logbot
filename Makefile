DOCKER_IMAGE ?= ankoh/logbot:latest

image:
	docker build -t $(DOCKER_IMAGE) -f docker/Dockerfile .

install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

tests:
	python -m tests.runner

.PHONY: install freeze tests
