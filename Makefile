init:
	pip3 install --user vex
	vex --make mugloar

deps:
	vex mugloar pip3 install --upgrade -r requirements.txt

test:
	vex mugloar tox

.PHONY: init deps test
