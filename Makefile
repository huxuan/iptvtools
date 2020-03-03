.PHONY: clean install dev flake8 pylint lint dist upload uploadtest test docs

PKG := $(shell basename $(CURDIR) | cut -d- -f1)
PIPRUN := $(shell command -v pipenv > /dev/null && echo pipenv run)

clean:
	find . -name '*.pyc' -print0 | xargs -0 rm -f
	find . -name '*.swp' -print0 | xargs -0 rm -f
	find . -name '.DS_Store' -print0 | xargs -0 rm -rf
	find . -name '__pycache__' -print0 | xargs -0 rm -rf
	rm -rf build dist *.egg-info .eggs || true
	rm -rf .tox .coverage cover || true
	rm -rf docs/_build || true
	rm -rf Pipfile.lock || true
	rm -rf .vscode || true
	command -v pipenv > /dev/null && \
		pipenv --venv > /dev/null 2>&1 && \
		pipenv --rm || true

install:
	command -v pipenv > /dev/null && \
		pipenv install --skip-lock -e . || \
		pip install -e .

dev:
	command -v pipenv > /dev/null && \
		pipenv install --skip-lock --dev || true

flake8:
	${PIPRUN} flake8 \
		--import-order-style google \
		--application-import-names ${PKG} \
		setup.py tests ${PKG}

pylint:
	${PIPRUN} pylint setup.py tests ${PKG}

lint: dev flake8 pylint

dist: clean install
	${PIPRUN} python setup.py sdist bdist_wheel

upload:
	${PIPRUN} twine upload dist/*

uploadtest:
	${PIPRUN} twine upload --repository-url https://test.pypi.org/legacy/ dist/*

docs: install
	cd docs && ${PIPRUN} make html

test: clean
	tox
