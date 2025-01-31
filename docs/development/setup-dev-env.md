# Set Up Development Environment

This page shows the approach to set up development environment. To simplify the process, a unified `Makefile` is maintained at the root directory of the repo. In other words, all the `make` related commands are supposed to run there.

## Prerequisites

[pipx](https://pipx.pypa.io/) is required to manage the standalone tools used across the development lifecycle.
Please refer to pipx's installation instructions [here](https://pipx.pypa.io/stable/installation/).
Once pipx is set up, install the needed standalone tools with the following command:

```bash
make prerequisites
```

## Setup

Development environment can be setup with the following command:

```bash
make dev
```

This command will accomplish the following tasks:

- Create a virtual environment.
- Install all the dependencies, including those for documentation, lint, package and test.
- Install the project in editable mode.
- Install git hook scripts for `pre-commit`.

To speed up the setup process in certain scenarios, you may find <project:/advanced/partial-dev-env.md> helpful.
