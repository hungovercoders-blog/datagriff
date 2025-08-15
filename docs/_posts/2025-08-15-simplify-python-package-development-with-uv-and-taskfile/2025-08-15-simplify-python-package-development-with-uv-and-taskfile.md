---
title: "Simplify Python Package Development with UV and Taskfile"
date: 2025-08-15
author: dataGriff
description: "Simplify Python Package Development with UV and Taskfile"
image:
  path: assets/2025-08-15-simplify-python-package-development-with-uv-and-taskfile/link.png
tags: Python UV Taskfile
---

I'd never made a python package before and I was keenly aware of my mismanagement of python environments in the past, especially after a few beers. Leveraging the power of [UV](https://docs.astral.sh/uv/){:target="\_blank"} I was quickly able to create a virtual environment and manage my dependencies with a sobering ease.Combining this with [Taskfile](https://taskfile.dev/){:target="\_blank"} allowed me to further simplify my development processes with abstractions for all my commands. This also allowed me to leverage very easily the same commands for local development and my CI!

## Pre-Requisites

- [VS Code](https://code.visualstudio.com/download){:target="\_blank"}
- [Github Account](https://github.com/){:target="\_blank"}
- [Git](https://git-scm.com/downloads){:target="\_blank"}
- [Python](https://www.python.org/downloads/){:target="\_blank"}
- [Curl](https://curl.se/download.html){:target="\_blank"}

I'll be leveraging codespaces as part of the setup for this demo and you can find the most up to date version of this at [https://github.com/hungovercoders/template.python.package](https://github.com/hungovercoders/template.python.package).

## Create a Python Package with UV

[UV](https://docs.astral.sh/uv/){:target="\_blank"} is a single tool that will replace all your python package management and virtual environment concerns of the past. Its written in rust and is designed to be fast and efficient. I used to end up with virtual environments all over the shop or my own machine bloated with python versions and libraries I no longer recognised due to my lazy hungover ways. This is no longer the case with [UV](https://docs.astral.sh/uv/){:target="\_blank"}...

### Install UV

You can [install UV](https://docs.astral.sh/uv/getting-started/installation/) in a number of ways including pip install.

```bash
pipx install uv
```

or a curl request and execution

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Once you have it installed confirm the version with

```bash
uv --version
```

![UV Install]({{ site.baseurl }}/assets/2025-08-15-simplify-python-package-development-with-uv-and-taskfile/uv_install.PNG)

### Initiate Package

Next create your package using the `--package` argument for your uv init command. This means you are creating package.

```bash
uv init --package hungovercoders_demo
```

![UV Install]({{ site.baseurl }}/assets/2025-08-15-simplify-python-package-development-with-uv-and-taskfile/uv_initiate_package.PNG)

You can also initiate apps, libraries or completely bare python projects using uv. Use the following command to see what's on offer.

```bash
uv init --help
```

### Lint the Package

### Test the Package

## Create a Github Action

## Introduce a Task File

## Simplify Github Action
