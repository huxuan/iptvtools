# CI/CD Configurations

The CI/CD (Continuous Integration and Continuous Delivery) workflows automate various development tasks to ensure project maintainability with minimal human effort. The configuration files are located at `.github/workflows/*.yml` for GitHub and `.gitlab/workflows/*.yml` for GitLab.

## `ci.yml`

The `ci` workflow is the most frequently used workflow, running on all pull/merge requests and changes to the default `main` branch. It performs linting, testing, and builds for the documentation and the package across all supported operation systems and Python versions to ensure everything works as expected.

## `commitlint.yml`

The `commitlint` workflow checks whether the pull/merge request title comply with the <project:/development/commit.md>. This ensures consistent commit history and enable the possibility of automated release pipeline.

## `delete-untagged-packages.yml`

The `delete-untagged-packages` workflow removes untagged packages since GitHub will still keep the package when overridden with the same tag. It helps keep the GitHub Packages clean and tidy.

## `devcontainer.yml`

The `devcontainer` workflow will be triggered by container related changes. It builds and tests the development and production containers and push the development container except during pull/merge requests, ensuring seamless containerized environments.

## `readthedocs-preview.yml`

The `readthedocs-preview` workflow leverage the [readthedocs/actions/preview](https://github.com/readthedocs/actions/tree/v1/preview) to add Read the Docs preview links to the related pull requests. These links make it easy to review documentation changes.

## `release.yml`

The `release` workflow manages the entire publish process, including publishing the documentation, containers and packages. It is triggered by a new release or a release tag. It also ensures all the builds and tests are succeed before completing the release.

## `renovate.yml`

The `renovate` workflow automates the <project:/management/update.md>. It is scheduled to run weekly and will create pull/merges request when there are new versions of the scaffold template, Python packages, GitHub Runners, GitHub Actions, docker images and etc. It keeps the project secure and ensures compatibility with the latest versions.

## `semantic-release.yml`

The `semantic-release` workflow automate the versioning and release process by publishing new releases or new release tags when certain changes are pushed to the default `main` branch. It simplifies the release management while maintaining consistency.
