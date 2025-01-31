# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12

########################################################################################
# Dev image is used for development and cicd.
########################################################################################

FROM python:${PYTHON_VERSION} AS dev

# NOTE: python docker image has env `PYTHON_VERSION` but with patch version.
# ARG is used here for temporary override without changing the original env.
ARG PYTHON_VERSION

# Config Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONHASHSEED=0
ENV PYTHONUNBUFFERED=1

# Config pipx
ENV PIPX_HOME=/usr/local/pipx
ENV PIPX_BIN_DIR=/usr/local/bin
ENV PIPX_DEFAULT_PYTHON=/usr/local/bin/python

# renovate: depName=debian_12/bash-completion
ARG BASH_COMPLETION_VERSION="1:2.11-6"
# renovate: depName=debian_12/pipx
ARG PIPX_VERSION="1.1.0-1"
# renovate: depName=debian_12/sudo
ARG SUDO_VERSION="1.9.13p3-1+deb12u1"
# renovate: depName=debian_12/vim
ARG VIM_VERSION="2:9.0.1378-2"

# Install system dependencies and override pipx with a newer version
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash-completion="${BASH_COMPLETION_VERSION}" \
    pipx="${PIPX_VERSION}" \
    sudo="${SUDO_VERSION}" \
    vim="${VIM_VERSION}" \
    && pipx install pipx==1.7.1 \
    && apt-get purge -y --autoremove pipx \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* \
    && hash -r

# Install prerequisites
RUN --mount=source=Makefile,target=Makefile \
    make prerequisites

# Create a non-root user with sudo permission
ARG USERNAME=iptvtools
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --create-home --uid $USER_UID --gid $USER_GID $USERNAME -s /bin/bash \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Set permission for related folders
RUN chown -R $USER_UID:$USER_GID $PIPX_HOME $PIPX_BIN_DIR

# Set default working directory
WORKDIR /workspace

########################################################################################
# Build image is an intermediate image used for building the project.
########################################################################################

FROM dev AS build

# Install dependencies and project into the local packages directory.
ARG SCM_VERSION
RUN --mount=source=README.md,target=README.md \
    --mount=source=pdm.lock,target=pdm.lock \
    --mount=source=pyproject.toml,target=pyproject.toml \
    --mount=source=src,target=src,rw \
    mkdir __pypackages__ && SETUPTOOLS_SCM_PRETEND_VERSION_FOR_IPTVTOOLS=${SCM_VERSION} pdm sync --prod --no-editable

########################################################################################
# Prod image is used for deployment and distribution.
########################################################################################

FROM python:${PYTHON_VERSION}-slim AS prod

# NOTE: python docker image has env `PYTHON_VERSION` but with patch version.
# ARG is used here for temporary override without changing the original env.
ARG PYTHON_VERSION

# Config Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONHASHSEED=0
ENV PYTHONUNBUFFERED=1

# Retrieve packages from build stage.
ENV PYTHONPATH=/workspace/pkgs
COPY --from=build /workspace/__pypackages__/${PYTHON_VERSION}/lib /workspace/pkgs

# Retrieve executables from build stage.
COPY --from=build /workspace/__pypackages__/${PYTHON_VERSION}/bin/* /usr/local/bin/

# Set command to run the cli by default.
ENTRYPOINT ["iptvtools-cli"]
