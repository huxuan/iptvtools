# Repository Settings

There are several settings to utilize the features provided by the project template. Although some of them are not strictly required, it is highly recommended finish these one-time jobs so as to benefit on the whole development lifecycle.

## Branch protection

::::{tab-set}

:::{tab-item} GitHub
:sync: github

1. Navigate to the [Branch protection rules](https://github.com/huxuan/iptvtools/settings/branches) settings.
1. Ensure a rule for the default `main` branch.
1. Enable **Require a pull request before merging** with **Require approvals** and **Dismiss stale pull request approvals when new commits are pushed** enabled.
1. Enable **Require status checks to pass before merging** and set [ci](https://github.com/huxuan/iptvtools/actions/workflows/ci.yml) and [commitlint](https://github.com/huxuan/iptvtools/actions/workflows/commitlint.yml) as required status checks.

:::

:::{tab-item} GitLab
:sync: gitlab

1. Navigate to the [Repository](https://gitlab.com/huxuan/iptvtools/-/settings/repository) settings and the **Protected branches** section.
1. Ensure the default `main` branch is protected with **Maintainers** for **Allowed to merge**, **No one** for **Allowed to push and merge** and **Allowed to force push** disabled.

:::
::::

## Tag protection

::::{tab-set}

:::{tab-item} GitHub
:sync: github

1. Navigate to the [Protected tags](https://github.com/huxuan/iptvtools/settings/tag_protection) settings.
1. Create a rule for tag name pattern `v*`.

:::

:::{tab-item} GitLab
:sync: gitlab

1. Navigate to the [Repository](https://gitlab.com/huxuan/iptvtools/-/settings/repository) settings and the **Protected tags** section.
1. Add a rule with wildcard `v*` for **Tag** and **Maintainers** for **Allowed to create**.

:::
::::

## Squash merge

::::{tab-set}

:::{tab-item} GitHub
:sync: github

1. Navigate to the [General](https://github.com/huxuan/iptvtools/settings) settings and the **Pull Requests** section.
1. Disable **Allow merge commits** and **Allow rebase merging**.
1. Enable **Allow squash merging** and set **Pull request title** as **Default commit message**.

:::

:::{tab-item} GitLab
:sync: gitlab

1. Navigate to the [Merge requests](https://gitlab.com/huxuan/iptvtools/-/settings/merge_requests) settings.
1. Set **Fast-forward merge** for the **Merge method**.
1. Set **Require** for the **Squash commits when merging**.
1. Enable **Pipelines must succeed** in the **Merge checks**.

:::
::::

## Pages

::::{tab-set}

:::{tab-item} GitHub
:sync: github

1. Navigate to the [GitHub Pages](https://github.com/huxuan/iptvtools/settings/pages) settings.
1. Set **GitHub Actions** as **Source**.

:::

:::{tab-item} GitLab
:sync: gitlab

Nothing need to do for GitLab Pages.

:::
::::

## Package publish

::::{tab-set}

:::{tab-item} GitHub
:sync: github

1. Navigate to the [Actions secrets and variables](https://github.com/huxuan/iptvtools/settings/secrets/actions) settings.
1. Set the **variable** `PDM_PUBLISH_REPO`, the repository (package index) URL to upload the package which defaults to `https://pypi.org`, the official PyPI.
1. Set the **variable** `PDM_PUBLISH_USERNAME`, the username to authenticate to the repository (package index) which defaults to `__token__`, used for [API token](https://pypi.org/help/#apitoken).
1. Set the **secret** `PDM_PUBLISH_PASSWORD`, the password to authenticate to the repository (package index).

:::

:::{tab-item} GitLab
:sync: gitlab

1. Navigate to the [CI/CD](https://gitlab.com/huxuan/iptvtools/-/settings/ci_cd) settings and the **Variables** section.
1. Set the variable `PDM_PUBLISH_REPO`, the repository (package index) URL to upload the package, default to `https://pypi.org`, the official PyPI.
1. Set the variable `PDM_PUBLISH_USERNAME`, the username to authenticate to the repository (package index), default to `__token__`, used for [API token](https://pypi.org/help/#apitoken).
1. Set the variable `PDM_PUBLISH_PASSWORD` with the **Mask variable** option for security, the password to authenticate to the repository (package index).

:::
::::

## Renovate and semantic-release

::::::{tab-set}

:::::{tab-item} GitHub
:sync: github

There are two approaches, either with GitHub App or with personal access token (classic). GitHub App is the more recommended way to avoid the issues and pull requests tied to a particular user.

::::{tab-set}

:::{tab-item} GitHub App

  1. [Register a GitHub App](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app) with permission listed [here](https://docs.renovatebot.com/modules/platform/github/#running-as-a-github-app) and `Repository administration: write` permission as mentioned [here](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/configuring-tag-protection-rules#about-tag-protection-rules).
  1. [Generate a private key](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/managing-private-keys-for-github-apps#generating-private-keys), and download the private key as a `.pem` file.
  1. Navigate to the [Actions secrets and variables](https://github.com/huxuan/iptvtools/settings/secrets/actions) settings.
  1. Set **App ID** of the GitHub App as **variable** `BOT_APP_ID`.
  1. Set the content of the private key as **secret** `BOT_PRIVATE_KEY`.

:::

:::{tab-item} personal access token (classic)

1. [Create a personal access token (classic)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic) with **workflow** scope.
1. Navigate to the [Actions secrets and variables](https://github.com/huxuan/iptvtools/settings/secrets/actions) settings and set the token as a **secret** `PAT`.

:::
::::

```{note}
You can set the scope of the variables and secrets to **Repository** or **Organization** according to actual requirements.
```

:::::

:::::{tab-item} GitLab
:sync: gitlab

Either [Group access tokens](https://docs.gitlab.com/ee/user/group/settings/group_access_tokens.html), [Project access tokens](https://docs.gitlab.com/ee/user/project/settings/project_access_tokens.html) or [Personal access tokens](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) can be used. The group or project access tokens are more recommended to avoid the issues and merge requests tied to particular user.

1. Create a [group access token](https://gitlab.com/groups/huxuan/-/settings/access_tokens), [project access token](https://gitlab.com/huxuan/iptvtools/-/settings/access_tokens) or [personal access token](https://gitlab.com/-/user_settings/personal_access_tokens) with `Maintainer` role and `api, write_repository` scope.
1. Navigate to the [CI/CD](https://gitlab.com/huxuan/iptvtools/-/settings/ci_cd) settings and the **Variables** section. Set the token as variable `PAT` with the **Mask variable** option for security.
1. Navigate to the [Pipeline schedules](https://gitlab.com/huxuan/iptvtools/-/pipeline_schedules). Create a new schedule with `*/15 0-3 * * 1` as **Interval Pattern** and mark it as **Activated**.

```{note}
Although optional, [creating a personal access token (classic)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic) on **GitHub** is strongly recommended. This token only needs `read-only` access and will increase the rate limit for Renovate to fetch dependencies and changelogs from github.com. It can be from any account and should be set as the variable `GITHUB_COM_TOKEN` with the **Mask variable** option for security. For more information on setting this up, see [Renovate's documentation](https://docs.renovatebot.com/getting-started/running/#githubcom-token-for-changelogs).
```

:::::
::::::
