.PHONY: clean deepclean install dev prerequisites mypy ruff ruff-format pyproject-fmt codespell lint pre-commit test-run test build publish doc-watch doc-build doc-coverage doc
########################################################################################
# Variables
########################################################################################

# Documentation target directory, will be adapted to specific folder for readthedocs.
PUBLIC_DIR := $(shell [ "$$READTHEDOCS" = "True" ] && echo "$${READTHEDOCS_OUTPUT}html" || echo "public")

# Determine the Python version used by pipx.
PIPX_PYTHON_VERSION := $(shell `pipx environment --value PIPX_DEFAULT_PYTHON` -c "from sys import version_info; print(f'{version_info.major}.{version_info.minor}')")

########################################################################################
# Development Environment Management
########################################################################################

# Remove common intermediate files.
clean:
	-rm -rf \
		$(PUBLIC_DIR) \
		.coverage \
		.mypy_cache \
		.pdm-build \
		.pdm-python \
		.pytest_cache \
		.ruff_cache \
		Pipfile* \
		__pypackages__ \
		build \
		coverage.xml \
		dist
	find . -name '*.egg-info' -print0 | xargs -0 rm -rf
	find . -name '*.pyc' -print0 | xargs -0 rm -f
	find . -name '*.swp' -print0 | xargs -0 rm -f
	find . -name '.DS_Store' -print0 | xargs -0 rm -f
	find . -name '__pycache__' -print0 | xargs -0 rm -rf

# Remove pre-commit hook, virtual environment alongside intermediate files.
deepclean: clean
	if command -v pre-commit > /dev/null 2>&1; then pre-commit uninstall; fi
	if command -v pdm >/dev/null 2>&1 && pdm venv list | grep -q in-project ; then pdm venv remove --yes in-project >/dev/null 2>&1; fi

# Install the package in editable mode.
install:
	pdm install --prod

# Install the package in editable mode with specific optional dependencies.
dev-%: install
	pdm install --lockfile pdm.dev.lock --no-default --dev --group $*

# Prepare the development environment.
# Install the package in editable mode with all optional dependencies and pre-commit hook.
dev: install
	pdm install --lockfile pdm.dev.lock --no-default --dev
	if [ "$(CI)" != "true" ] && command -v pre-commit > /dev/null 2>&1; then pre-commit install; fi

# Lock both prod and dev dependencies.
lock:
	pdm lock --prod --update-reuse-installed
	pdm lock --lockfile pdm.dev.lock --no-default --dev --update-reuse-installed

# Install standalone tools
prerequisites:
	pipx list --short | grep -q "check-jsonschema 0.31.0" || pipx install --force check-jsonschema==0.31.0
	pipx list --short | grep -q "codespell 2.4.1" || pipx install --force codespell[toml]==2.4.1
	pipx list --short | grep -q "pdm 2.22.3" || pipx install --force pdm==2.22.3
	pipx list --short | grep -q "pre-commit 4.1.0" || pipx install --force pre-commit==4.1.0
	pipx list --short | grep -q "pyproject-fmt 2.5.0" || pipx install --force pyproject-fmt==2.5.0
	pipx list --short | grep -q "ruff 0.9.3" || pipx install --force ruff==0.9.3
	pipx list --short | grep -q "watchfiles 1.0.4" || pipx install --force watchfiles==1.0.4

########################################################################################
# Lint and pre-commit
########################################################################################

# Check lint with mypy.
mypy:
	pdm run python -m mypy . --html-report $(PUBLIC_DIR)/reports/mypy

# Lint with ruff.
ruff:
	ruff check .

# Format with ruff.
ruff-format:
	ruff format --check .

# Check lint with pyproject-fmt.
pyproject-fmt:
	pyproject-fmt pyproject.toml

# Check lint with codespell.
codespell:
	codespell

# Check jsonschema with check-jsonschema.
check-jsonschema:
	check-jsonschema --builtin-schema vendor.github-workflows .github/workflows/*.yml
	check-jsonschema --builtin-schema vendor.readthedocs .readthedocs.yaml
	check-jsonschema --builtin-schema vendor.renovate --regex-variant nonunicode .renovaterc.json

# Check lint with all linters.
lint: mypy ruff ruff-format pyproject-fmt codespell check-jsonschema

# Run pre-commit with autofix against all files.
pre-commit:
	pre-commit run --all-files --hook-stage manual

########################################################################################
# Test
########################################################################################

# Clean and run test with coverage.
test-run:
	pdm run python -m coverage erase
	pdm run python -m coverage run -m pytest

# Generate coverage report for terminal and xml.
test: test-run
	pdm run python -m coverage report
	pdm run python -m coverage xml

########################################################################################
# Package
########################################################################################

# Build the package.
build:
	pdm build

# Publish the package.
publish:
	pdm publish

########################################################################################
# Documentation
########################################################################################

# Generate documentation with auto build when changes happen.
doc-watch:
	pdm run python -m http.server --directory public &
	watchfiles "make doc-build" docs src README.md

# Build documentation only from src.
doc-build:
	pdm run sphinx-build --fail-on-warning --write-all docs $(PUBLIC_DIR)

# Generate html coverage reports with badge.
doc-coverage: test-run
	pdm run python -m coverage html -d $(PUBLIC_DIR)/reports/coverage
	pdm run bash scripts/generate-coverage-badge.sh $(PUBLIC_DIR)/_static/badges

# Generate all documentation with reports.
doc: doc-build mypy doc-coverage

########################################################################################
# End
########################################################################################
