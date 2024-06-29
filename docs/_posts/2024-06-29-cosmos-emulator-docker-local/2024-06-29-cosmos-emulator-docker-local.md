---
title: "Developing locally with cosmos emulator in a container"
date: 2024-06-29
author: dataGriff
description: Developing locally with cosmos emulator in a container
image:
  path: /assets/2024-06-29-cosmos-emulator-docker/link.png
tags: Docker Azure Cosmos
---

A problem came up recently whereby we needed to run the cosmos emulator in a docker container for local development and subsequently in the CI stage of our deployment pipeline to reduce the need for a permanent environment. This was a right head scratcher and started to make me feel worse than a classic hungovercoder hangover. There was only way to cure myself of this... Solve the problem with my favourite of all hangover cures - doggos! Lets jump in and demonstrate how we can create a local developer experience with a dotnet app and the cosmo emulator running docker.

- [Pre-Requisites](#pre-requisites)


## Pre-Requisites

In order to carry out this walkthrough you'll need the following:

- [Github Account](https://github.com/){:target="_blank"}
- [VS Code](https://code.visualstudio.com/download){:target="_blank"}

For development on your local machine your going to need the following tools installed:

- [DotNet](https://dotnet.microsoft.com/en-us/download/dotnet-framework){:target="_blank"}
- [Git](https://git-scm.com/downloads){:target="_blank"}
- [Docker Desktop](https://www.docker.com/products/docker-desktop/){:target="_blank"}
- [Curl](https://help.ubidots.com/en/articles/2165289-learn-how-to-install-run-curl-on-windows-macosx-linux){:target="_blank"}

However, I am again using the mighty [gitpod](https://gitpod.io/) to cater for these needs and my docker file looks like this (I'm using this as a base for other Azure dotnet work which is why there are other things in there - handy though right??).

```Dockerfile
FROM gitpod/workspace-dotnet

USER gitpod

# Install Homebrew
RUN /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" && \
    echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> ~/.bashrc

# Update Homebrew, Install Terraform & Azure CLI
RUN eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)" && \
    brew update && \
    brew tap hashicorp/tap && \
    brew install hashicorp/tap/terraform && \
    brew upgrade terraform && \
    brew install azure-cli  && \
    brew install aztfexport && \
    brew install maven

# Install Azure Functions Core Tools
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && \
    sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg && \
    sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-ubuntu-$(lsb_release -cs)-prod $(lsb_release -cs) main" > /etc/apt/sources.list.d/dotnetdev.list' && \
    sudo apt-get update && \
    sudo apt-get install azure-functions-core-tools-4
```

And my gitpod yaml looks like this

```yaml
image:
  file: .cde.Dockerfile

vscode:
  extensions:
    - hashicorp.terraform
    - ms-azuretools.vscode-azureresourcegroups
    - formulahendry.code-runner
    - gitpod.gitpod-desktop
    - ms-dotnettools.csdevkit
    - patcx.vscode-nuget-gallery
    - ms-vscode.azurecli
```

Now that was so easy. Did I mention I love gitpod?

## Compose your Cosmos Emulator

