# Partially Set Up Development Environment

In certain cases, it is unnecessary to install all dependencies as well as the pre-commit hook. For example, this can speed up the setup process in CI/CD.

## Minimal installation

Install the project in editable mode with only the necessary dependencies, which is useful for scenarios like deployment.

```bash
make install
```

## Documentation generation

Install the project in editable mode with dependencies related to `doc`,
recommended for scenarios like the documentation generation CI/CD process.

```bash
make dev-doc
```

## Lint check

Install the project in editable mode with dependencies related to `lint`,
recommended for scenarios like the lint CI/CD process.

```bash
make dev-lint
```

## Package build

Install the project in editable mode with dependencies related to `package`,
recommended for scenarios like the package CI/CD process.

```bash
make dev-package
```

## Testing

Install the project in editable mode with dependencies related to `test`,
recommended for scenarios like the test CI/CD process.

```bash
make dev-test
```

## Combination

To install dependencies for `doc` and `lint`, use the following command:

```bash
make dev-doc,lint
```
