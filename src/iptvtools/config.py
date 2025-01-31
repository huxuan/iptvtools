#!/usr/bin/env python
"""Configuration for iptvtools.

File: config.py
Author: huxuan
Email: i(at)huxuan.org
"""

import json
import os
import os.path
from pathlib import Path
from typing import Any


class MetaConfig(type):
    """Configuration for iptvtools."""

    config: dict[str, Any] = {}

    @classmethod
    def init(cls, config_file: str | Path) -> None:
        """Initialize configuration."""
        if os.path.isfile(config_file):
            with open(config_file) as fin:
                cls.config = json.load(fin)

    def __getattr__(cls, key: str) -> Any:
        """Get configuration with key."""
        return cls.config.get(key, {})


class Config(metaclass=MetaConfig):  # pylint: disable=R0903
    """Configuration for iptvtools."""
