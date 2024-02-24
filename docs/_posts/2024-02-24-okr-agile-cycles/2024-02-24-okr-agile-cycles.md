---
title: "Integrating OKR Cycles into the Agile Framework"
date: 2024-02-24
author: dataGriff
description: Integrating OKR Cycles into the Agile Framework
image:
  path: /assets/2024-02-24-okr-agile-cycles/link.png
tags: OKR Agile
---

It's been nearly 2 years since I posted one of my [first blogs which was around OKRs (objectives and key results)](https://blog.hungovercoders.com/datagriff/2022/09/17/team-okr-hdd.html){:target="_blank"}. Since then I have been preaching their usage and loving the concept... but I have completely missed integrating their ideas into the day to day agile working practices, rendering them ineffective. Spurred on by co-workers, my will to ensure that prioritisation of value is easy during iteration ceremonies, and the awesome book [Succeeding with OKRs in Agile](https://www.amazon.co.uk/Succeeding-OKRs-Agile-deliver-objectives-ebook/dp/B0CGXLGL74){:target="_blank"}, below are my thoughts on how to integrate OKR cycles into the agile framework.

- [Prerequisites](#prerequisites)
- [Hungovercoders Github Template](#hungovercoders-github-template)
- [Linking a Repo to a Project](#linking-a-repo-to-a-project)
- [Method 1: Project Automation](#method-1-project-automation)
- [Method 2: Template Issues and Bugs](#method-2-template-issues-and-bugs)
- [Method 3: Github Actions](#method-3-github-actions)

## Why Integrate OKRs with Agile

* Focus on outcomes over output
* Bottom up engagement over top down
* Ease of prioritisation of value during iteration ceremonies
* Self-motivation and autonomy

## OKRs gone Wrong

* Bottom up engagement over top down control


## Making OKRs Everything...

If you are going to do OKRs I recommend just using them for everything - except renumeration

## ...Except Renumeration

The goals of every team member should simply be to help the team achieve their OKRs. However a persons individual renumeration should not be associated with the teams OKRs. This may sound counter-intuitive but as soon as you introduce individuals goals as being a driver for OKRs you will inevitably get gaming of the system ([Goldharts Law](https://en.wikipedia.org/wiki/Goodhart%27s_law#:~:text=Goodhart's%20law%20%5B...%5D,people%20start%20to%20game%20it.)) and so the very purpose of OKRs is lost. OKRs are meant to drive ownership and the enjoyment of solving a shared problem, if you start isolating the outcomes to individual performance of each team member you will lose the core aspect of a team contributing to a shared goal.

How then do you solve the problem of awarding people for their individual performance when so much of their day to day is wrapped up in the team OKRs? My approach would be to link self-development, team and community goals to the individuals performance. These three categories can be related to how they may impact OKRs but should not be directly linked to them. This way you can still reward people for their individual performance but not at the expense of the sharing of the team based goals that are the OKRs. Performance rewards here can not only be based on how they did against the tasks they set out for themselves, but also the tasks they chose and what foresight they held to know how they could help their own team or the wider communities. You could ask these questions to team members in order to spark ideas for their self-development, team and community goals:

- **What skills do you want to develop?**
  - I can learn automated testing (so that I can improve the quality and throughput of the team to meet their OKRs)  
- **What can you do to support the team?**
  - I can automate that manual scaling process (so that I can save my team members time and give them more time to focus on OKRs) 
- **What can you do to support the community?**
  - I can demonstrate how we query our alerts (so that other teams can also see more quickly their reliability metrics and improve their OKRs) 

## OKR and Agile Cycle

## OKR Ceremonies

```mermaid!
gantt
title Integrated OKR and Agile Sprint Schedule
dateFormat  YYYY-MM-DD
excludes weekends

section Planning
OKR Ideation: 2023-12-18, 2023-12-18
OKR Creation: 2023-12-25, 2023-12-26
OKR Impact Planning: 2023-12-27, 2023-12-27

section Iteration 1
Daily Stand-ups: 2024-01-01, 2024-01-17
Zero Tolerance: 2024-01-08, 2024-01-08
Backlog Refinement: 2024-01-08, 2024-01-08
Zero Tolerance: 2024-01-15, 2024-01-15
Backlog Refinement: 2024-01-15, 2024-01-15
Iteration Review: 2024-01-18, 2024-01-18
Iteration Retrospective: 2024-01-18, 2024-01-18
Iteration Planning: 2024-01-18, 2024-01-18

section Iteration 2
Daily Stand-ups: 2024-01-19, 2024-01-31
Zero Tolerance: 2024-01-22, 2024-01-22
Backlog Refinement: 2024-01-22, 2024-01-22
Zero Tolerance: 2024-01-29, 2024-01-29
Backlog Refinement: 2024-01-29, 2024-01-29
Iteration Review: 2024-02-01, 2024-02-01
Iteration Retrospective: 2024-02-01, 2024-02-01
Iteration Planning: 2024-02-01, 2024-02-01

section Iteration 3
Daily Stand-ups: 2024-02-02, 2024-02-15
Zero Tolerance: 2024-02-05, 2024-02-05
Backlog Refinement: 2024-02-05, 2024-02-05
Zero Tolerance: 2024-01-29, 2024-01-29
Backlog Refinement: 2024-01-29, 2024-01-29
Iteration Review: 2024-02-01, 2024-02-01
Iteration Retrospective: 2024-02-01, 2024-02-01
Iteration Planning: 2024-02-01, 2024-02-01

section Closing
OKR Retrospective: 2024-03-22, 2024-03-22

section Next
OKR Ideation: 2024-03-18, 2024-03-18
OKR Creation: 2024-03-25, 2024-03-26
OKR Impact Planning: 2024-03-27, 2024-03-27
```

### OKR Ideation

#### Categories of Concern

### OKR Creation

### OKR Impact Planning

### OKR Retrospective

## Iteration Ceremonies

### Daily Stand-ups

### Backlog Refinement

### Iteration Review

### Iteration Planning

## Zero Tolerance

## Work Item Types and Tagging

### Work Item Types

### Work Item Tags

#### Value Tags

#### Concern Tags

#### General Tags
