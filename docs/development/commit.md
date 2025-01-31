# Commit Convention

Using structured commit messages, we can enhance the readability of our project history, simplify automated changelog generation, and streamline the release process. We primarily follow the [Conventional Commit](https://www.conventionalcommits.org/) and [Angular's commit guidelines](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commits).

## Commit Message Pattern

```text
<type>(<optional scope>): <description>
```

Examples:

```text
build(dependencies): bump the prod group with 9 updates.
doc: Add doc for commit convention.
chore: remove deprecated key in ruff config.
```

Type
: Describes the nature of the change:

| Type      | Description                                            |
|-----------|--------------------------------------------------------|
| `build`   | Changes that affect the build system or dependencies.  |
| `chore`   | Routine tasks or changes outside the src/runtime code. |
| `ci`      | Changes related to continuous integration.             |
| `doc`     | Documentation changes.                                 |
| `feat`    | New features.                                          |
| `fix`     | Bug fixes.                                             |
| `perf`    | Performance improvements.                              |
| `refactor`| Code restructuring without changing behavior.          |
| `revert`  | Revert a previous commit.                              |
| `style`   | Code formatting changes.                               |
| `test`    | Add or update tests.                                   |

Scope [Optional]
: Represents the part of the project impacted by the change. Examples include `logging`, `settings`, and `cli`.

### Breaking Change

A "breaking change" refers to any modification that disrupts the existing functionality in a way that may affect users. It can be denoted using an exclamation mark (`!`) before the colon, like `refactor!: Stuff`.

## Commit in Development Branches

While the commit convention seems strict, we aim for flexibility during the development phase.
By adhering to the <project:/management/settings.md>, all changes should be introduced via pull/merge requests.
Using the squash merge strategy, the emphasis is primarily on the title of pull/merge requests.
In this way, individual commit within development branches does not need to strictly adhere to the commit convention.

````{note}
A CI/CD pipeline checks the titles of pull/merge requests against the following regex pattern:

```text
^(build|chore|ci|doc|feat|fix|perf|refactor|revert|style|test)(\(\w+\))?!?:\s.*
```
````
