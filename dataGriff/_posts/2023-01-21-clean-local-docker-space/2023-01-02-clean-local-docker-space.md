---
title: "Save Space on you Local Docker"
date: 2023-01-22

author: dataGriff
---

Super quick blog post today which will help stop you screaming at your C drive when it runs out of space for more beer downloads.

To clear out your local docker images and then reduce down the space taken on your machine run the following commands in a terminal.

First to remove unused docker containers...

```bash
docker system prune -a
```

Then reduce the data found in C:\Users\{user}\AppData\Local\Docker\wsl\data\ext4.vhdx run the following:

```bash
wsl --shutdown
diskpart
```

You'll get the diskspace pop up in another prompt then run this in that terminal:

```bash
select vdisk file="C:\Users\{user}\AppData\Local\Docker\wsl\data\ext4.vhdx"
attach vdisk readonly
compact vdisk
detach vdisk
exit
```

You should see the ext4.vhdx file reduces down plenty and frees you up to continue those massive windows updates.

Happy space saving!
