# IPTVTools

A set of scripts that help to better IPTV experience.

[![CI](https://github.com/huxuan/iptvtools/actions/workflows/ci.yml/badge.svg)](https://github.com/huxuan/iptvtools/actions/workflows/ci.yml)
[![CommitLint](https://github.com/huxuan/iptvtools/actions/workflows/commitlint.yml/badge.svg)](https://github.com/huxuan/iptvtools/actions/workflows/commitlint.yml)
[![DevContainer](https://github.com/huxuan/iptvtools/actions/workflows/devcontainer.yml/badge.svg)](https://github.com/huxuan/iptvtools/actions/workflows/devcontainer.yml)
[![Release](https://github.com/huxuan/iptvtools/actions/workflows/release.yml/badge.svg)](https://github.com/huxuan/iptvtools/actions/workflows/release.yml)
[![Renovate](https://github.com/huxuan/iptvtools/actions/workflows/renovate.yml/badge.svg)](https://github.com/huxuan/iptvtools/actions/workflows/renovate.yml)
[![Semantic Release](https://github.com/huxuan/iptvtools/actions/workflows/semantic-release.yml/badge.svg)](https://github.com/huxuan/iptvtools/actions/workflows/semantic-release.yml)
[![Coverage](https://img.shields.io/endpoint?url=https://huxuan.github.io/iptvtools/_static/badges/coverage.json)](https://huxuan.github.io/iptvtools/reports/coverage)
[![Release](https://img.shields.io/github/v/release/huxuan/iptvtools)](https://github.com/huxuan/iptvtools/releases)
[![PyPI](https://img.shields.io/pypi/v/iptvtools)](https://pypi.org/project/iptvtools/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/iptvtools)](https://pypi.org/project/iptvtools/)
[![GitHub](https://img.shields.io/github/license/huxuan/iptvtools)](https://github.com/huxuan/iptvtools/blob/main/LICENSE)

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm-project.org)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/5697b1e4c4a9790ece607654e6c02a160620c7e1/docs/badge/v2.json)](https://pydantic.dev)
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-orange.json)](https://github.com/copier-org/copier)
[![Serious Scaffold Python](https://img.shields.io/endpoint?url=https://serious-scaffold.github.io/ss-python/_static/badges/logo.json)](https://serious-scaffold.github.io/ss-python)
[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/huxuan/iptvtools)

> [!IMPORTANT]
> _IPTVTools_ is in the **Beta** phase.
> Changes and potential instability should be anticipated.
> Any feedback, comments, suggestions and contributions are welcome!

## Features

Scripts currently provided:

- iptvtools-cli filter
  - Merge from different resources.
  - Check the tcp/udp connectivity.
  - Filter by custom criteria, e.g. resolution.
  - Match with templates and EPG.
  - Format the url with UDPxy if provided.
  - Unify channels' titles.

Features planned on the road:

- [ ] Scan certain ip and port range to find new channels.
- [ ] Establish a lightweight database for routine maintenance.

Besides, all scripts should be lightweight and able to keep running regularly after proper configuration.

Last but not least, any ideas, comments and suggestions are welcome!

## Prerequisites

To filter by stream information, e.g., resolution/height, [ffmpeg](https://www.ffmpeg.org/) (or [ffprobe](https://www.ffmpeg.org/ffprobe.html) more precisely) is needed, please install according to the [documentation](https://www.ffmpeg.org/download.html).

## Installation

It is recommended to manage iptvtools via [pipx](https://github.com/pypa/pipx):

```shell
pipx install iptvtools
```

## Usage

Please refer to the [documentation](https://iptvtools.readthedocs.io/) while some useful information in [wiki](https://github.com/huxuan/iptvtools/wiki).
## 📜 License

MIT License, for more details, see the [LICENSE](https://github.com/huxuan/iptvtools/blob/main/LICENSE) file.
