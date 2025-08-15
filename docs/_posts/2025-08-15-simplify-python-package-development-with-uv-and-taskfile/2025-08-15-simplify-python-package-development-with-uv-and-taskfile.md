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
uv init --package
```

![UV Install]({{ site.baseurl }}/assets/2025-08-15-simplify-python-package-development-with-uv-and-taskfile/uv_initiate_package.PNG)

You can provide a name for the package as an argument as well, but I have deliberately not provided one so that toml file ends up in the root along with the src directory. This does mean your github repo naming is important to reflect the name of the package. This later allows us to treat the github repo directly as a package and we can install from it using pip install without needing to publish to pypi. This is very handy for a quick turnaround and testing of our package!

You can also initiate apps, libraries or completely bare python projects using uv. Use the following command to see what's on offer.

```bash
uv init --help
```

### Run the package locally

The package comes initiated with one main method in the code `src/hungovercoders_demo/__init__.py`

```python
def main() -> None:
    print("Hello from demo-python-package!")
```

To try this out we can run the package using uv

```bash
uv run demo-python-package
```

![UV Run Package]({{ site.baseurl }}/assets/2025-08-15-simplify-python-package-development-with-uv-and-taskfile/uv_run_package.PNG)

Uv will automatically create a virtual environment for you (woop! woop!) and create a uv.lock file. The uv.lock file will ensure consistent environments for anyone who uses your package.

### Convert the Package into a CLI

Next we're going to convert the package into a CLI. Keeping this simple for the demo we'll leverage the simple greetings package laid out in [packaging python]({:target="_blank"}){:target="\_blank"} - [creating and packaging command-line tools](https://packaging.python.org/en/latest/guides/creating-command-line-tools/){:target="\_blank"}, and tweak it to make it slightly simpler. The package will leverage the [typer](https://typer.tiangolo.com/){:target="\_blank"} library which makes creating a CLI tool even easier.

First create a `greetings.py` file and add the following code

```python
import typer
from typing_extensions import Annotated


def greet(
    name: Annotated[str, typer.Option(help="The name of the person to greet")] = ""
):
    greeting = f"Hello {name}!"
    print(greeting)
```

This means we're going to expose a command called greet that takes a `--name` option as a parameter then prints this out to the terminal.

Then add a `cli.py` file and add the following code

```python
import typer

from .greetings import greet


app = typer.Typer()
app.command()(greet)


if __name__ == "__main__":
    app()
```

This means we're creating a typer application and adding the greet command we defined in greetings. We're then going to expose this typer application through our main entry point.

Then add a `main.py` file and add the following code

```python
if __name__ == "__main__":
    from demo_python_package.cli import app
    app()
```

This imports the app into the main entry point and allows us to run the CLI.

We'll remove all the code from the `__init__.py` file. We still need the file to mark the directory as a package.

We then need to update the `pyproject.toml` file to include an entry point for the script and include a dependency on [typer](https://typer.tiangolo.com/){:target="\_blank"}. By adding typer as a dependency UV will automatically install this into our virtual environment for us.

```toml
##...
dependencies = ["typer"]

[project.scripts]
demo-python-greet = "demo_python_package.cli:app"
###..
```

Finally to install and test the cli locally we can run the following to install it locally

```bash
uv pip install . e
```

then run the following to see it work based off the alias we gave it in the toml

```bash
uv run demo-python-greet --name griff
```

![UV Run Package]({{ site.baseurl }}/assets/2025-08-15-simplify-python-package-development-with-uv-and-taskfile/uv_run_cli.PNG)

### Lint the Package

Next up we can lint our python package using [ruff](https://docs.astral.sh/ruff/){:target="\_blank"}. This is also brought to us by the same people as UV so is extremely fast and lightweight.

Run the following to perform the ruff checks.

```bash
uvx ruff check
```

![Ruff Check Pass]({{ site.baseurl }}/assets/2025-08-15-simplify-python-package-development-with-uv-and-taskfile/ruff_check_pass.PNG)

These are all passing which is a bit boring, so lets break some linting rules, such as an f -string without any variable, and run it again. Now we get an error.

![Ruff Failure]({{ site.baseurl }}/assets/2025-08-15-simplify-python-package-development-with-uv-and-taskfile/ruff_failure.PNG)

We can fix this by running

```bash
uvx ruff check --fix
```

![Ruff Fix]({{ site.baseurl }}/assets/2025-08-15-simplify-python-package-development-with-uv-and-taskfile/ruff_fix.PNG)

Next run uv build so we can get the packaged up wheel files and ensure that they are also pass linting checks correctly.

```bash
uv build
```

These will be created in the `dist` directory.

Then run the following to ensure that the files built all have the appropriate metadata as part of the lint checks.

```bash
uvx twin
```

![Ruff Pass]({{ site.baseurl }}/assets/2025-08-15-simplify-python-package-development-with-uv-and-taskfile/ruff_pass.PNG)

Right we're looking good from a linting point of view, lets move on to testing!

### Test the Package

## Create a Github Action

## Introduce a Task File

## Simplify Github Action
