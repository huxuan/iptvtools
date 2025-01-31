# Clean Up Development Environment

When encountering environment-related problems, a straightforward solution is to cleanup the environment and setup a new one. Three different levels of cleanup approach are provided here.

## Intermediate cleanup

Intermediate cleanup only removes common intermediate files, such as generated documentation, package, coverage report, cache files for mypy, pytest, ruff and so on.

```bash
make clean
```

## Deep cleanup

Deep cleanup removes the pre-commit hook and the virtual environment alongside the common intermediate files.

```bash
make deepclean
```

## Complete cleanup

Complete cleanup restores the repository to its original, freshly-cloned state, ideal for starting over from scratch.

```{caution}
This will remove all untracked files, please use it with caution. It is recommended to check with dry-run mode (`git clean -dfnx`) before actually removing anything. For more information, please refer to the [git-clean documentation](https://git-scm.com/docs/git-clean).
```

```bash
git clean -dfx
```
