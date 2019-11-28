# iptv-m3u-filter

Filter iptv m3u playlist for customization.

Quite a few publicly available IPTV channels can be found on the Internet, but usually only a part of them is valuable considering accessibility, resolution, latency, bandwidth and some other criteria.

This script aims to help with that filtering process.

## Prerequisites

```shell
make deps
```

or

```shell
pip install -r requirements.txt
```

## Usage

```shell
$ python main.py -h
usage: main.py [-h] [--min-height MIN_HEIGHT] [-i INPUT] [-o OUTPUT]
               [-p MAX_WORKERS] [-t TIMEOUT]

optional arguments:
  -h, --help            show this help message and exit
  --min-height MIN_HEIGHT
                        Minimal acceptable height/resolution, defaults to 1080
                        which means 1080P.
  -i INPUT, --input INPUT
                        Valid M3U playlists, which could be a file or url,
                        defaults to `https://iptv-
                        org.github.io/iptv/index.m3u`.
  -o OUTPUT, --output OUTPUT
                        Output file name, defaults to `iptv-m3u-filter.m3u`.
  -p MAX_WORKERS, --max-workers MAX_WORKERS
                        Number of threads to perform the filtering process,
                        defaults to 16.
  -t TIMEOUT, --timeout TIMEOUT
                        Acceptable timeout when retrieving stream information,
                        defaults to 2.
```

## Roadmap

> Any help is welcome for the following topics.

- [ ] Upload to PyPI.
- [ ] Support strategies to unify channel titles. For example, covert `CCTV1`, `CCTV-1HD`, `CCTV-1FHD` to `CCTV-1综合`.
- [ ] Support template combination, such as the [test.m3u](http://epg.51zmt.top:8000/test.m3u) under http://epg.51zmt.top:8000/.
- [ ] Support regular execution, may not by Python code, but usage or documentation instead.
- [ ] Support online deployment, scripts may needed, but still may not by Python code.
- [ ] Support more criteria if possible.
- [ ] Better documentation/docstrings.
- [ ] i18n support.
