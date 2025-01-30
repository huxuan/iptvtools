#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Configuration for iptvtools.

File: config.py
Author: huxuan
Email: i(at)huxuan.org
"""
import json
import os
import os.path


class MetaConfig(type):
    """Configuration for iptvtools."""

    config = {}

    @classmethod
    def init(cls, config_file):
        """Initialize configuration."""
        if os.path.isfile(config_file):
            with open(config_file) as fin:
                cls.config = json.load(fin)

    def __getattr__(cls, key):
        """Get configuration with key."""
        return cls.config.get(key, {})


class Config(metaclass=MetaConfig):  # pylint: disable=R0903
    """Configuration for iptvtools."""
