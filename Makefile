.PHONY: clean install dev lint pycodestyle pyflakes pylint dist upload docs

clean:
	find . -name '*.pyc' -print0 | xargs -0 rm -f
	find . -name '*.swp' -print0 | xargs -0 rm -f
	find . -name '.DS_Store' -print0 | xargs -0 rm -rf
	find . -name '__pycache__' -print0 | xargs -0 rm -rf
	-rm -rf build dist *.egg-info .eggs *.spec docs/_build

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

dist: clean
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/*

docs: clean install
	cd docs && make html

docsdeps:
	pip install -r docs/requirements.txt
