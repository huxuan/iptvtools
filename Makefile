.PHONY: clean install dev lint pycodestyle pyflakes pylint dist upload

clean:
	find . -name '*.pyc' -print0 | xargs -0 rm -f
	find . -name '*.swp' -print0 | xargs -0 rm -f
	find . -name '.DS_Store' -print0 | xargs -0 rm -rf
	find . -name '__pycache__' -print0 | xargs -0 rm -rf
	-rm -rf build dist *.egg-info .eggs *.spec

install:
	pip install .

dev:
	pip install .[dev]

lint: pycodestyle pyflakes pylint

pycodestyle:
	-pycodestyle setup.py iptvtools

pyflakes:
	-pyflakes setup.py iptvtools

pylint:
	-pylint setup.py iptvtools

dist:
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/*
