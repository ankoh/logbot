#----------------------------------------------------
.PHONY: freeze
freeze:
	pip freeze > requirements.txt
#-----------------------------------------------------
.PHONY: tests
tests:
	python -m tests.runner
#-----------------------------------------------------