# dataGriff Blog

- [dataGriff Blog](#datagriff-blog)
  - [Create New Post](#create-new-post)
  - [Run Locally](#run-locally)
  - [Useful Code](#useful-code)
    - [Escape Curly Brackets](#escape-curly-brackets)
    - [Markdown Open New Tab](#markdown-open-new-tab)

## Create New Post

Amend the variables in `create_post.py` to be appropriate for your new blog post.

```py
blog_title = "Blog Title One"
tags = ["Tag1", "Tag2", "Tag3"]
author = "dataGriff"
```

Run the create post script.

```bash
python create_post.py
```

## Run Locally

```bash
cd docs
bundle exec jekyll serve
```

## Useful Code

### Escape Curly Brackets

{% raw %}{{ place }}{% endraw %}

### Markdown Open New Tab

{:target="\_blank"}
