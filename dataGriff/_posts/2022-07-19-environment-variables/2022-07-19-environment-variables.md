---
title: "Utilizing User Environment Variables"
date: 2022-07-19

author: dataGriff
---

Creating environment variables is useful for when you want to use the same variable across multiple languages or perhaps to maintain a consistent environment for your settings on your machine, such as development credentials.

First create your environment variable in windows by doing the following:

1. Edit the environment variables for your account.
2. Create a new environment variable and give it a value.

![Environment Variables]({{ site.url }}/assets/images/environment_var.PNG)

To access and print the variable in bash from the command-line:

```bash
echo %MY_VARIABLE%
```

To access and print the variable in Powershell:

```powershell
Write-Output([System.Environment]::GetEnvironmentVariable('MY_VARIABLE'))
```

To access and print the variable in python:

```python
import os
print(os.environ.get('MY_VARIABLE'))
```

To access and print the variable in C#:

```c#
Console.WriteLine(System.Environment.GetEnvironmentVariable("MY_VARIABLE"));
```
