# Project Initialization

## Prerequisites

[pipx](https://pipx.pypa.io/) is required to manage the standalone tools used across the development lifecycle.
Please refer to pipx's installation instructions [here](https://pipx.pypa.io/stable/installation/).
Once pipx is set up, install the copier for project generation using the following command:

```bash
pipx install copier==9.4.1
```

## Create the Repository

Create a blank Git repository on the hosting platform. Clone it locally and navigate to the root directory:

```bash
git clone git@github.com:huxuan/iptvtools.git
cd iptvtools
```

## Generate the Project

Running the following command and answer the prompts to set up the project:

```bash
copier copy gh:serious-scaffold/ss-python .
```

## Set Up Development Environment

Set up development environment to prepare for the initial commit:

```bash
make dev
```

## Commit and push

```bash
git add .
git commit -m "chore: init from serious-scaffold-python"
SKIP=no-commit-to-branch git push
```

Now, everything is done!
