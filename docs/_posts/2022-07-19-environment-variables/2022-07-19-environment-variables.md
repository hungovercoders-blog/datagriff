---
title: "Utilizing User Environment Variables"
date: 2022-07-19
author: dataGriff
description: Using local environment variables for repeat usage in code such as python, .net, powershell and bash
image:
  path: /assets/2022-07-19-environment-variables/link.png
tags: python powershell .net bash
---

Creating environment variables is useful for when you want to use the same variable across multiple languages, or perhaps to maintain a consistent environment for your settings on your machine, such as development credentials.

First create your environment variable in windows by doing the following:

- Edit the environment variables for your account.

![Environment Variables]({{ site.baseurl }}/assets/2022-07-19-environment-variables/edit_environment_var.PNG)

- Create a new environment variable and give it a value.

![Environment Variables]({{ site.baseurl }}/assets/2022-07-19-environment-variables/environment_var.PNG)

### Bash

To access and print the variable in bash from the command-line:

```bash
echo %MY_VARIABLE%
```

### Powershell

To access and print the variable in Powershell:

```powershell
Write-Output([System.Environment]::GetEnvironmentVariable('MY_VARIABLE'))
```

### Python

To access and print the variable in python:

```python
import os
print(os.environ.get('MY_VARIABLE'))
```

### C#

To access and print the variable in C#:

```c#
Console.WriteLine(System.Environment.GetEnvironmentVariable("MY_VARIABLE"));
```
