# Tests

In the context of CI/CD automation, dependency updates, and the release process, tests play a crucial role in daily development. We utilize [pytest](https://docs.pytest.org/) and [coverage](https://coverage.readthedocs.io) with proper configuration to ensure everything works as expected. This page provides general information and conventions we wish you to follow.

## Running Tests

After [setting up the development environment](/development/setup-dev-env.md), tests can be run with the command:

```bash
make test
```

With the default configuration, this command displays the result for each test case, the execution time for slow test cases, and a report on test coverage.

## Writing Tests

For guidelines on how to write tests, refer to [the official documentation](https://docs.pytest.org/how-to/assert.html). Here are some conventions we expect you to follow:

1. Organize all test cases under the `tests` directory.
2. Align test modules with the modules to be tested.

   For example, tests for the `iptvtools.cli` module should be located in the file `tests/cli_test.py`. If there are too many test cases, they can be split into files within the `tests/cli/` directory, using a prefix for each test file.
3. Unless necessary, do not lower the threshold of the test coverage.

## Coverage Report

After running the tests, the coverage report will be printed on the screen and generated as part of the documentation. You can view it [here](/reports/coverage/index.md).
