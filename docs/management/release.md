# Release Process

With the integration of [semantic-release](https://github.com/semantic-release/semantic-release), the release process is fully automated. To enable this, follow the settings for <project:/management/settings.md#renovate-and-semantic-release>. Besides, adhering to the <project:/development/commit.md#commit-message-pattern> is strongly recommended to ensure the release process works as expected.

## Release Configuration

The release configuration is located in the root directory of the project:

```{literalinclude} ../../.releaserc.json
```

Based on this configuration, the following trigger rules apply:

* A **major** release is triggered by a 'BREAKING CHANGE' or 'BREAKING-CHANGE' in the footer or has a `major-release` scope.
* A **minor** release is triggered when the commit type is `feat` or has a `minor-release` scope.
* A **patch** release is triggered when the commit type is `fix`, `perf`, `refactor` or `revert` or has a `patch-release` scope.
* No release is triggered if the commit type is any other type or has a `no-release` scope.

## Commit message examples

### Major release

* ```text
  feat: drop Python 3.8 support

  BREAKING CHANGE: drop Python 3.8 support
  ```
* `chore(major-release): a major release`

### Minor release

* `feat: add an awesome feature`
* `chore(minor-release): a minor release`

### Patch release

* `fix: fix a silly bug`
* `perf: performance improvement for the core`
* `refactor: refactor the base module`
* `revert: revert a buggy implementation`
* `chore(patch-release): a patch release`

### No release

* `feat(no-release): a feature that should not trigger a release`
* `fix(no-release,core): a fix that should not trigger a release, but with more scopes`

## Release Tasks

The release process includes the following tasks:

::::{tab-set}

:::{tab-item} GitHub
:sync: github

1. Generate a changelog from unreleased commits.
1. Publish a new GitHub Release and semantic version tag.
1. Build and publish the documentation to GitHub Pages.
1. Build and publish the Python package to the configured package repository.
1. Build and publish the Development and Production Containers with the build cache to GitHub Packages.
    1. The Production Container is tagged as `ghcr.io/huxuan/iptvtools:py<PYTHON_VERSION>` for the latest version and `ghcr.io/huxuan/iptvtools:py<PYTHON_VERSION>-<PROJECT_VERSION>` for archives.
    1. The Development Container is tagged as `ghcr.io/huxuan/iptvtools/dev:py<PYTHON_VERSION>` for the latest version and `ghcr.io/huxuan/iptvtools/dev:py<PYTHON_VERSION>-<PROJECT_VERSION>` for archives.
    1. The build cache for the Development Container is tagged as `ghcr.io/huxuan/iptvtools/dev-cache:py<PYTHON_VERSION>`.

:::

:::{tab-item} GitLab
:sync: gitlab

1. Generate a changelog from unreleased commits.
1. Publish a new GitLab Release and semantic version tag.
1. Build and publish the documentation to GitLab Pages.
1. Build and publish the Python package to the configured package repository.
1. Build and publish the Development and Production Containers with build cache to GitLab Container Registry.
    1. The Production Container is tagged as `registry.gitlab.com/huxuan/iptvtools:py<PYTHON_VERSION>` for the latest version and `registry.gitlab.com/huxuan/iptvtools:py<PYTHON_VERSION>-<PROJECT_VERSION>` for archives.
    1. The Development Container is tagged as `registry.gitlab.com/huxuan/iptvtools/dev:py<PYTHON_VERSION>` for the latest version and `registry.gitlab.com/huxuan/iptvtools/dev:py<PYTHON_VERSION>-<PROJECT_VERSION>` for archives.
    1. The build cache for the Development Container is tagged as `registry.gitlab.com/huxuan/iptvtools/dev-cache:py<PYTHON_VERSION>`.

:::

::::
