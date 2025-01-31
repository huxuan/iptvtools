# Git Workflow

This pages shows the recommended Git workflow to keep the local repository clean and organized while ensuring smooth collaboration among team members.

## Prerequisites

Make sure you have [Git](https://git-scm.com/) (version 2.23 and above) installed and properly configured especially for authentication.

## Fork and clone the repository

Fork the repository to your own namespace, and let us take `https://github.com/<username>/iptvtools` as example.

Clone the repository and navigate to the root directory:

```shell
git clone git@github.com:<username>/iptvtools.git
cd iptvtools
```

## Configure the remote

Add and update the `upstream` remote repository:

```shell
git remote add upstream https://github.com/huxuan/iptvtools
git fetch upstream
```

Configure `git` to pull `main` branch from the `upstream` remote:

```shell
git config --local branch.main.remote upstream
```

Configure `git` never to push to the `upstream` remote:

```shell
git remote set-url --push upstream git@github.com/<username>/iptvtools.git
```

## Verify the remote configuration

List the remote repositories with urls:

```shell
git remote -v
```

You should have two remote repositories: `origin` to your forked CPython repository, and `upstream` pointing to the official CPython repository:

```shell
origin  git@github.com:<username>/iptvtools.git (fetch)
origin  git@github.com:<username>/iptvtools.git (push)
upstream        https://github.com/huxuan/iptvtools (fetch)
upstream        git@github.com:<username>/iptvtools.git (push)
```

Note that the push url of `upstream` repository is the forked repository.

Show the upstream for `main` branch:

```shell
git config branch.main.remote
```

You should see `upstream` here.

## Work on a feature branch

Create and switch to a new branch from `main`:

```shell
git switch -c <branch-name> main
```

Stage the changed files:

```shell
git add -p # to review and add changes to existing files
git add <filename1> <filename2> # to add new files
```

Commit the staged files:

```shell
git commit -m "the commit message"
```

Push the committed changes:

```shell
git push
```

## Create a pull request

Navigate to the hosting platform and create a pull request.

After the pull request is merged, you need to delete the branch in your namespace.

```{note}
It is recommended to configure the automatic deletion of the merged branches.
```

## Housekeeping the cloned repository

Update the `main` branch from upstream:

```shell
git switch main
git pull upstream main
```

Remove deleted remote-tracking references:

```shell
git fetch --prune origin
```

Remove local branches:

```shell
git branch -D <branch-name>
```

After all these operations, you should be ready to <project:#work-on-a-feature-branch> again.

## Reference

- [Git bootcamp and cheat sheet, Python Developer's Guide](https://devguide.python.org/getting-started/git-boot-camp/)
