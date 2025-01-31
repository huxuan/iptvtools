# Development Container

Instead of manually configuring your development environment, [Dev Containers](https://containers.dev/) offer a seamless containerized development experience right out of the box.

## Prerequisites

Before you can use a Dev Container, you will need to install a few components.

1. [Docker Desktop](https://www.docker.com/products/docker-desktop) or an [alternative Docker option](https://code.visualstudio.com/remote/advancedcontainers/docker-options).
1. [Visual Studio Code](https://code.visualstudio.com/).
1. The [Dev Containers extension](vscode:extension/ms-vscode-remote.remote-containers) within VSCode.

## Usage

After installing the prerequisites, you have two main approaches to use a Dev Container. Using [a locally cloned repository](#open-a-locally-cloned-repository-in-a-container) leverages your existing local source code, while [an isolated container volume](#open-the-repository-in-an-isolated-container-volume) creates a separate copy of the repository, which is particularly useful for PR reviews or exploring branches without altering your local environment.

### Open a locally cloned repository in a container

When you open a repository that includes a Dev Container configuration in VS Code, you will receive a prompt to reopen it in the container.

```{image} /_static/images/dev-container-reopen-prompt.png
:alt: Dev Container Reopen Prompt.
```

If you missed the prompt, you can use the **Dev Containers: Reopen in Container** command from the Command Palette to initiate the containerized environment. Here are some frequently used commands:

Dev Containers: Reopen in Container
: Triggers the containerized environment setup upon opening a repository configured for Dev Containers.

Dev Containers: Rebuild Without Cache and Reopen in Container
: Useful for refreshing your environment in case of issues or to update to a newer version.

Dev Containers: Clean Up Dev Containers...
: Deletes stopped Dev Container instances and removes unused volumes, helping maintain a clean development environment.

### Open the repository in an isolated container volume

You may already notice the badge [![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/huxuan/iptvtools) in the [Overview](/index.md) page. You can click the badge or [this link](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/huxuan/iptvtools) to get started. Clicking these links will cause VS Code to automatically install the Dev Containers extension if needed, clone the source code into a container volume, and spin up a dev container for use.

## Reference

For more detailed guidance and advanced usage, explore the following resources:

- [Dev Containers tutorial](https://code.visualstudio.com/docs/devcontainers/tutorial)
- [Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers)
