from datetime import datetime
from pathlib import Path

blog_title = "Protecting Code Quality with Trunk.io"
tags = ["Git", "VSCode", "Trunk.io"]
author = "dataGriff"

print("Start creating blog title...")
blog_file_title = blog_title.lower().replace(" ", "-")
date = datetime.today().strftime("%Y-%m-%d")
date_blog = f"{date}-{blog_file_title}"
print("Completed creating blog title.")

print("Start creating post directory...")
post_directory = f"/workspace/datagriff/docs/_posts/{date_blog}"
Path(post_directory).mkdir(parents=True, exist_ok=True)
print("Completed creating post directory.")

print("Start creating asset directory...")
asset_directory = f"/workspace/datagriff/docs/assets/{date_blog}"
Path(asset_directory).mkdir(parents=True, exist_ok=True)
image_directory = f"/workspace/datagriff/docs/assets/{date_blog}/link.png"
print("Completed creating asset directory.")

print("Start creating blog file paths...")
post_file = f"{date_blog}.md"
post_full_path = f"{post_directory}/{post_file}"
tags_string = " ".join(tags)
print("Completed creating blog file paths.")

print("Start creating blog file and content...")
with open(f"{post_full_path}", "w") as file:
    file.write(
        f"""---
title: "{blog_title}"
date: {date}
author: {author}
description: "{blog_title}"
image:
  path: {image_directory}
tags: {tags_string}
---

Introductory text

## Pre-Requisites

- [VS Code](https://code.visualstudio.com/download){{:target="\_blank"}}
- [Github Account](https://github.com/){:target="\_blank"}
- [Git](https://git-scm.com/downloads){:target="\_blank"}

As always I will be using the mighty [gitpod](https://gitpod.io){{:target="\_blank"}} so I won't need to configure anything other than spinning up a workspace.

## Section 1

Text goes here

![Image Description]({{ site.baseurl }}/assets/{date_blog}/image-01.PNG)
"""
    )
print("Completed creating blog file and content.")
