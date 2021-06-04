# MAKEFILE

PYTHON = python3

all: run

run:
	${PYTHON} src/main.py

lint:
	flake8 src/

typehint:
	pytype src/

checklist: lint typehint

clean:
	${RM} -r log
	find . -type f -name "*.pyc" | xargs ${RM}
	find . -type d -name "__pycache__" | xargs ${RM} -r
	find . -type d -name ".pytype" | xargs ${RM} -r
	find . -type d -name "cache" | xargs ${RM} -r

.PHONY = run lint typehint checklist clean
