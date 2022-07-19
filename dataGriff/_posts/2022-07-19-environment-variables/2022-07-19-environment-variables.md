---
title: "Utilizing environment variables"
date: 2022-07-19

author: dataGriff
---



```bash
print ("%MY_VARIABLE%")
```


```python
print(os.environ.get('MY_VARIABLE'))
```

```powershell
print([System.Environment]::GetEnvironmentVariable('MY_VARIABLE'))
```

```c#
Environment.GetEnvironmentVariable("MY_VARIABLE")
```
