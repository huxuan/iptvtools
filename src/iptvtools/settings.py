"""Settings Module."""

import logging
from logging import getLevelName

from pydantic_settings import BaseSettings, SettingsConfigDict


class GlobalSettings(BaseSettings):
    """System level settings."""

    ci: bool = False
    """Indicator for whether or not in CI/CD environment."""


class Settings(BaseSettings):
    """Project specific settings."""

    logging_level: str | None = getLevelName(logging.INFO)
    """Default logging level for the project."""

    model_config = SettingsConfigDict(
        env_prefix="IPTVTOOLS_",
    )


# NOTE(huxuan): `#:` style docstring is required for module attributes to satisfy both
# autodoc [1] and `check-docstring-first` in `pre-commit` [2].
# [1] https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#directive-autoattribute
# [2] https://github.com/pre-commit/pre-commit-hooks/issues/159#issuecomment-559886109

#: Instance for system level settings.
global_settings = GlobalSettings()

#: Instance for project specific settings.
settings = Settings()
