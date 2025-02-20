#!/usr/bin/env python
"""Custom exceptions for iptvtools.

File: exceptions.py
Author: huxuan
Email: i(at)huxuan.org
"""


class BaseCustomException(RuntimeError):
    """Base Custom Exception."""


class FFmpegNotInstalledError(BaseCustomException):
    """Raise when FFmpeg is not installed."""

    def __init__(self) -> None:
        """Init for FfmpegNotInstalledError."""
        super().__init__(
            "Need `FFmpeg` for resolution related processing.\n"
            "Please install it according to "
            "`https://www.ffmpeg.org/download.html`."
        )
