---
title: "Turbo charging your conventional git commit workflow in VS Code"
date: 2024-08-13
author: dataGriff
description: Turbo charging your conventional git commit workflow in VS Code
image:
  path: /assets/2024-08-13-git-conventional-vs-code-workflow/link.png
tags: Git VSCode
---

I was recently introduced to [git conventional commits](https://www.conventionalcommits.org/en/v1.0.0/){:target="_blank"} as a method of streamlining your logged messages and providing the ability to automatically generate [CHANGELOG](https://github.com/marketplace/actions/generate-changelog-based-on-conventional-commits){:target="_blank"}. My first instinct these days is to quickly search for a [VS Code extension](https://marketplace.visualstudio.com/vscode){:target="_blank"} on any new language or topic I am given. Lo and behold I had a [hit](https://marketplace.visualstudio.com/items?itemName=vivaxy.vscode-conventional-commits){:target="_blank"}! After some preference tweaking, as recommended by the extension, and a new (but old) keyboard shortcut, I now bring to you my turbocharge git conventional commit workflow in VS code!

- [Pre-Requisites](#pre-requisites)
- [End Goal](#end-goal)
- [Install VS Code Extension](#install-vs-code-extension)
- [Set the Following Preferences in VS Code](#set-the-following-preferences-in-vs-code)
- [Ctrl + S](#ctrl--s)

## Pre-Requisites

In order to carry out this walkthrough you'll need the following:

- [Github Account](https://github.com/){:target="_blank"}
- [Git](https://git-scm.com/downloads){:target="_blank"}
- [VS Code](https://code.visualstudio.com/download){:target="_blank"}
- [VS Code Conventional Commit Extension](https://code.visualstudio.com/download){:target="_blank"} - We will install this as part of the blog post. 

As always I will be using the mighty [gitpod](https://gitpod.io){:target="_blank"} so I won't need to configure anything other than spinning up a workspace.

## End Goal

1. I want to easily use conventional commit styles in my commit messages.
1. I want to add all staged files and sync easily with my remote.
1. I want a keyboard shortcut that makes sense to perform all of this seamlessly.

## Install VS Code Extension

Part one turned out to be really easy! All I needed to do was install the [VS Code Conventional Commit Extension](https://code.visualstudio.com/download){:target="_blank"}! This easily accessible from the command palette (CTRL+P) by searching for "conventional commit". This takes you the process  of providing a good [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/){:target="_blank"} with prompts and dropdown lists to help you apply all the standard conventions. This is fantastic news for me as my memory is often suspect these days with my whiskey addled mind becoming less and less reliable.

The extension will prompt for:

1. Adding the type.
2. Adding the scope.
3. Adding an emoji.
4. Adding the short message.
5. Adding the long message.
6. Adding details on whether it was a breaking change.

The settings are all configurable as per the [extension docs](https://code.visualstudio.com/download){:target="_blank"}.

## Set the Following Preferences in VS Code

To make your workflow even slicker you can set the conventional commits extension plus vs code to automatically stage and sync any commits you decide to make. All of this taken from the recommendations in the [extension docs](https://code.visualstudio.com/download){:target="_blank"}. It really does pay to read the documentation sometimes...

In File > Preferences > Settings of VS Code set conventionalCommits.autoCommit to be true. The default is already true but just double check. This will attempt to commit any changes when you go through the extension workflow above, but if you have not staged your files it will prompt you to stage them in a dialog box and you also have to remember to sync. That's 2 things extra to do! I simply couldn't cope with this extra cognitive load.

![Conventional Commits Autocommit]({{ site.baseurl }}/assets/2024-08-13-git-conventional-vs-code-workflow/conventional-commit-autocommit.PNG)

Following on from the extension recommendations, in File > Preferences > Settings of VS Code enable git.smartCommitChanges and set git.enableSmartCommit to be all. This will mean whenever you complete the conventional commit workflow now it will automatically stage and commit all files without the need for further prompts. Now how about that automatic sync...?

![Git Smart Commit]({{ site.baseurl }}/assets/2024-08-13-git-conventional-vs-code-workflow/git-smart-commit.PNG)

The last piece of the extension recommendations, in File > Preferences > Settings of VS Code set git.postCommitCommand to sync. This will mean every time you commit... you sync! No more lost code im remote locations and awesome commit messages to boot!

![Git Post Commit Sync]({{ site.baseurl }}/assets/2024-08-13-git-conventional-vs-code-workflow/git-post-commit-sync.PNG)

## Ctrl + S

I wanted to shortcut up the initiation of the conventional commit > commit > sync workflow to make it even easier for myself.

First I ensured autosave was on in VS code so I didn't have to constantly hit CTRL+S (though I do this anyway).

![VS Code Auto Save]({{ site.baseurl }}/assets/2024-08-13-git-conventional-vs-code-workflow/vs-code-auto-save.PNG)

Secondly I changed the keyboard shortcut for the conventional commit to be CTRL+S in my VS code preferences.

![VS Code Keyboard Shortcut]({{ site.baseurl }}/assets/2024-08-13-git-conventional-vs-code-workflow/vs-code-keyboard-shortcut.PNG)

Now every time I hit this combo I save the work, I then start the conventional commit workflow and when it ends - boom it commits then syncs. Living the dream!

![VS Code Conventional Commit Workflow]({{ site.baseurl }}/assets/2024-08-13-git-conventional-vs-code-workflow/conventional-commit-workflow.gif)

If I do decide I have committed to early I can simply press escape to carry on coding. However why would you ever not commit regularly to a remote...? Trunk based development I can imagine would require some [git hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks){:target="_blank"} to protect your commit which is something I might look at soon (see this [pre-commit](https://pre-commit.com/){:target="_blank"} which looks interesting). For feature branch development however I think this workflow is very handy for good commits, safely remotely stored code and fast feedback!
