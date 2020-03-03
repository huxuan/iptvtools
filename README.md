# IPTVTools

[![PyPI version](https://badge.fury.io/py/iptvtools.svg)](https://badge.fury.io/py/iptvtools)
[![Documentation Status](https://readthedocs.org/projects/iptvtools/badge/?version=latest)](https://iptvtools.readthedocs.io/en/latest/?badge=latest)
[![PyPI license](https://img.shields.io/pypi/l/iptvtools.svg)](https://pypi.python.org/pypi/iptvtools/)
[![Python Versions](https://img.shields.io/pypi/pyversions/iptvtools.svg)](https://pypi.python.org/pypi/iptvtools/)
[![Downloads](https://pepy.tech/badge/iptvtools)](https://pepy.tech/project/iptvtools)

Scripts currently provided:

- [iptv-filter](https://iptvtools.readthedocs.io/en/latest/scripts/iptv-filter.html)
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

```shell
pip install -U iptvtools
```

## Usage

Please refer to the [documentation](https://iptvtools.readthedocs.io/) while some useful information in [wiki](https://github.com/huxuan/iptvtools/wiki).
