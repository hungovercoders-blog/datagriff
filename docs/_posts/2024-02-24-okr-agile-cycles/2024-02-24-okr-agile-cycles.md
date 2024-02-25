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

- [Quick OKR and Agile Recap](#quick-okr-and-agile-recap)
- [Why Integrate OKRs with Agile](#why-integrate-okrs-with-agile)
- [Making OKRs Everything](#making-okrs-everything)
  - [Objective Zero](#objective-zero)
- [Team OKRs Should not Link to Individual Renumeration](#team-okrs-should-not-link-to-individual-renumeration)
- [The Football Analogy](#the-football-analogy)
- [OKR and Agile Cycle](#okr-and-agile-cycle)
- [OKR Ceremonies](#okr-ceremonies)
  - [OKR Scene Setting](#okr-scene-setting)
    - [Categories of Concern](#categories-of-concern)
  - [OKR Creation](#okr-creation)
  - [OKR Impact Planning](#okr-impact-planning)
  - [OKR Retrospective](#okr-retrospective)
- [Iteration Ceremonies](#iteration-ceremonies)
  - [Daily Stand-ups](#daily-stand-ups)
  - [Zero Tolerance](#zero-tolerance)
  - [Backlog Refinement](#backlog-refinement)
  - [Iteration Planning](#iteration-planning)
  - [Iteration Review](#iteration-review)
  - [Iteration Retrospective](#iteration-retrospective)
- [Stay Agile](#stay-agile)

## Quick OKR and Agile Recap

For OKRs I recommend reading my previous [blog post](https://blog.hungovercoders.com/datagriff/2022/09/17/team-okr-hdd.html){:target="_blank"} on the matter but just in case here is a quick refresher:

- OKRs stand for Objectives & Key Results.
- A team mission should help understand objectives for the lifecycle of the team and should be fairly static. 
- Objectives based on this mission should be agreed strategically with more senior members of the organisation and addressed about every 90 days. 
- The key results then should be time-bound and an agreed method of how you will measure the success of your objectives. These objectives and key results should almost be unattainable, but realistic enough to be aspirational for the team as well as stretching them.

For agile I recommend reading the [agile manifesto](https://agilemanifesto.org/){:target="_blank"} but with regards to this blog post I am referring to the ceremonies that are part of the agile framework. These ceremonies are:

- Backlog refinement where the team reviews the backlog and ensures that the work is ready for the next iteration.
- Sprint or iteration planning where the team decides what work they will do in the next iteration.
- Sprint or iteration review where the team reviews the work they have done in the last iteration.
- Sprint or iteration retrospective where the team reviews how they have worked in the last iteration and how they can improve.

There is no explicit link made between the two and this is what I aim to address in this blog post.

## Why Integrate OKRs with Agile

If you do not integrate your OKRs with the day to day workload usually managed by agile processes like Kanban or Scrum, then your establishment of OKRs were simply a waste. The goal of OKRs is to drive bottom up engagement over top down control and therefore it should be in the very fabric of your teams day to day work. If you have not created that link between OKRs and the agile ceremonies, then they will forever be treated as separate beasts where strategy and the execution of work items are not aligned. This creates the risk of losing the outcome orientated work established by OKRs in favour of ticket completion outputs favoured by short term iteration processes. By providing the alignment between the two you will be able to:

- Prioritise more easily during iteration ceremonies as you have taken the time to collectively establish prioritisation rules in advance via OKRs
- Focus on outcomes over output by ensuring that the work you are doing is aligned with th pre-agreed OKRs
- Ensure bottom up engagement over top down control by allowing the team to establish their own OKRs and then align their work to them
- Create a self-motivating team that is focused on shared goals rather than individual performance

![Michael Sheen]({{ site.baseurl }}/assets/2024-02-24-okr-agile-cycles/michael-sheen.jpg)

## Making OKRs Everything

If you are going to do OKRs I recommend just using them for everything - except individual renumeration ([see below](#team-okrs-should-not-link-to-individual-renumeration)). This is because one of the main purposes of OKRs is to make prioritisation easy when you are in the middle of your iterations. When you are in short-term work mode and deep into solving the problem that is immediately in front of you as part of your iterations, you are not taking the time to lookup as much you would like and prioritisation almost feels like a distraction. How many times you have yourself maybe groaned at the prospect of backlog refinement or iteration planning because you are in the middle of something and you just want to get it done? OKRs can help by making it far easier in these ceremonies to prioritise the work as a team as you have already spent the time in advance to establish and agree your OKRs. If something does not align with your OKRs then it is not a priority and you can move on. I'd recommend making no more than four objectives and aim for around three key results each. This provides a simple way for the team to focus by not overwhelming them with too much to remember.

**Objective 1**: Improve Whiskey Distillery Coverage

- **Key Result 1**: 100% of Scottish distilleries are available for online hungovercoder visitors to read by the end of the quarter.
- **Key Result 2**: 100% of Irish distilleries are available for online hungovercoder visitors to read by the end of the quarter.
- **Key Result 3**: One hungovercoder visitor has clicked a distillery link by the end of the quarter.
  
**Objective 2**: Improve Dog Rescue Coverage

- **Key Result 1**: 100% of Dogs Trust centres are available for online hungovercoder visitors to read by the end of the quarter.
- **Key Result 2**: 100% of Blue Cross centres are available for online hungovercoder visitors to read by the end of the quarter.
- **Key Result 3**: One hungovercoder visitor has clicked a dog rescue link by the end of the quarter.

**Objective 3**: Share Knowledge in Online Community

- **Key Result 1**: 2 Blog posts made available on hungovercoders by end of first month.
- **Key Result 2**: 4 Blog posts made available on hungovercoders by end of second month.
- **Key Result 3**: 6 Blog posts made available on hungovercoders by end of third month.

Looking at the above shows the clear focus and succinct nature of the OKRs. They are not overwhelming and they are not too detailed whilst maintaining a specificity that makes it easy for the team to prioristise their work as part of their agile iterations.

Notice as well that each of the key results has a numeric assignment to them. This is important because it can allow the partial completion of an objective which often may be enough. The key results should aim to stretch a team. For example asking for 20% of Scottish distilleries to be available by the end of the quarter may be very achievable, but if the team stops here and regard this as success, they may not get the opportunity to achieve 70% of coverage, which whilst unsuccessful compared to the 100% set out in the key result, is still a more significant improvement than asking for less originally. Make sure when you agree your key results you understand if they are a "must have" completion, such as the end of a contract, or if they are aspirational. I prefer the aspirational type but they should always be about 70-80% achievable at least so as not to become demotivating to the team.

Make sure that your OKRs are plastered across as many different places as possible so that each team member sees these at least daily. This can include your team homepage, team dashboards, work planning boards, desktop background or pinned communication messages to name but a few. The more you can make these visible the more likely they are to be front of mind when the team is working on their day to day tasks and be able to prioritise correctly when it comes to iteration ceremonies. I recommend having them readily available to other teams and senior management so they know what you are focused on and the reasons you have for saying "no" legitimately to requests that sit outside the bounds of these OKRs you have agreed.

What about work that we need to do that does not come as part of the more strategic OKRs...?

![Objective Zero]({{ site.baseurl }}/assets/2024-02-24-okr-agile-cycles/zero.png)

### Objective Zero

What about BAU or "keeping the lights on" type work? This is where you can create an "Objective Zero" as discussed in the book [Succeeding with OKRs in Agile](https://www.amazon.co.uk/Succeeding-OKRs-Agile-deliver-objectives-ebook/dp/B0CGXLGL74){:target="_blank"}. This describes treating your objective zero and its key results as a set of service level agreements (SLAs) that you need to maintain in order to keep the lights on. This way you can still have a set of OKRs that are strategic and aspirational and a set of OKRs that are more operational and tactical. It also highlights the tension between the two types of work and the need to balance them rather than "managing" BAU tickets separately to what you want to achieve strategically. It may even involve removing a strategic objective because of the realisation of this work.

**Objective Zero**: Ensure the team is able to maintain the current level of service

- **Key Result 1**: There are no critical software vulnerabilities by the end of the quarter.
- **Key Result 2**: There is a 99.95% uptime of our services by the end of the quarter.
- **Key Result 3**: There is no software with less than 3 months to end of life by the end of the quarter.

The fact that you will realise that you need an objective zero speaks volumes about its importance and I would potentially default to treating this objective as the most important when prioritising, but hopefully with the least amount of work. If you do find that your Objective Zero is consuming most of your strategic work, you likely need to revisit why as part of your OKR planning and bring in more focused objectives to solve the amount of time you need to spend on keeping the lights on. I love this idea to integrate this type of work as part of your OKRs and aim to satisfy the need to cover this work in the ceremony "[Zero Tolerance](#zero-tolerance)" below. Ensure your objective zero sits alongside any documentation or posts that you have for your OKRs so that it is clear the importance of this work and the need to balance it with your strategic OKR work.

## Team OKRs Should not Link to Individual Renumeration

**The goal of every team member should simply be to help the team achieve their OKRs.** I love the simplicity of this statement.

However a persons individual renumeration should not be associated with the teams OKRs. This may sound counter-intuitive but as soon as you introduce individuals goals as being a driver for OKRs you will inevitably get gaming of the system ([Goldharts Law](https://en.wikipedia.org/wiki/Goodhart%27s_law#:~:text=Goodhart's%20law%20%5B...%5D,people%20start%20to%20game%20it.)) and so the very purpose of OKRs is lost. OKRs are meant to drive ownership and the enjoyment of solving a shared problem, if you start isolating the outcomes to individual performance of each team member you will lose the core aspect of a team contributing to a shared goal.

![OKR Money]({{ site.baseurl }}/assets/2024-02-24-okr-agile-cycles/okr-money.png)

How then do you solve the problem of awarding people for their individual performance when so much of their day to day is wrapped up in the team OKRs? My approach would be to link self-development, team and community goals to the individuals performance. These three categories can be related to how they may impact OKRs but should not be directly linked to them. This way you can still reward people for their individual performance but not at the expense of the sharing of the team based goals that are the OKRs. Performance rewards here can not only be based on how they did against the tasks they set out for themselves, but also the tasks they chose and what foresight they held to know how they could help their own team or the wider communities. You could ask these questions to team members in order to spark ideas for their self-development, team and community goals:

- **What skills do you want to develop?** (how can you help the team as an individual)
  - I can learn automated testing (so that I can improve the quality and throughput of the team to meet their OKRs)  
- **What can you do to support the team?** (how can you help multiple individuals in the team)
  - I can automate that manual scaling process we have to do (so that I can save my team members time and give them more time to focus on OKRs)
- **What can you do to support the community?** (how can you help multiple teams)
  - I can demonstrate how we query our alerts to the wider community (so that other teams can also see more quickly observe their reliability metrics and improve their OKRs)

Below is an example of what an individuals OKRs could look like within the context of the team OKR examples set out above, that relate to publishing whiskies and dog rescues. The idea being that the individual recognises, and knows in advance, what kind of skills will be required to achieve the team OKRs, and along with suitable guidance agrees OKRs that will help them achieve these skills. This way the individual can have unique performance metrics attributed to them, but with the team in mind, allowing for personal advancement that is also aligned with the team goals. Remember - the goal of every team member should simply be to help the team achieve their OKRs.

**Objective**: Improve CRUD Application Delivery Knowledge

- **Key Result 1**: Certification in some document storage and retrieval by end of the quarter (helping the team as an individual).
- **Key Result 2**: Host a team tutorial on how to use the new document storage and retrieval system by end of the quarter (helping multiple individuals in the team).
- **Key Result 3**: Host a company wide tutorial on how to use the new document storage and retrieval system by end of the quarter (helping multiple teams).

## The Football Analogy

Whilst drinking a few beers with my friends, we discussed making the analogy between the team and the individual OKRs in software to a football team and a football player. We ended up with the following which I hope helps better explain how team OKRs and individual performance relate but also remain separate.

**Football Team Objective:** Become the best football club in Europe

- **Key Result 1**: Qualify for the Champions League by coming fourth or above in the league this season.
- **Key Result 2**: Win the quarter-final of the champions league next season.
- **Key Result 3**: Win the semi-final of the champions league next season.

Now an individual should not have their performance measured against the team objective, though they should support it, which will come from a combination of a professional individual and good guidance from leadership. For example...

**Football Player Objective:** Improve Assists at the Football Club

- **Key Result 1**: Improve pass accuracy in simulation to 95% by end of the season (helping the team as an individual)
- **Key Result 2**: Provide an average of 2 assists for goal scoring opportunities per game by end of the season (helping multiple individuals in the team)  
- **Key Result 3**: Provide one pass master class per month to the academy teams until the end of the season (helping multiple teams)

Hopefully this further demonstrates how you can allow an individual to succeed in the context of team OKRs but without explicitly having the two depend on one another.

![Football]({{ site.baseurl }}/assets/2024-02-24-okr-agile-cycles/football.jpg)

## OKR and Agile Cycle

Below is an example schedule of how you can setup your ceremonies to align with your OKR cycles. The example below setups up quarterly OKR cycles and fortnightly iterations, this is a very high level view and you may need to adjust the timings of these ceremonies to fit your own teams needs. If you are just starting OKRs it may be pertinent to try monthly cycles at first to get fast feedback on their efficacy and allowing you to change more often before committing to quarterly turnarounds. The good thing about getting this viewpoint is seeing how many iterations you actually have to deliver on your OKRs as they can often go by very quickly and value may not have been realised when it should have been.

The OKR ceremonies are setup to align with the start and end of the OKR cycle and the iteration ceremonies are setup to align with the start and end of the iteration cycle. The iteration cycles are driven by the OKRs established and the iterations are then just that, iterative progress against your objectives inline with the key results by which they have agreed to be measured.

@startmermaid
gantt
title Integrated OKR and Agile Sprint Schedule
dateFormat  YYYY-MM-DD
excludes weekends

section OKR Current Start
OKR Scene Setting: 2023-12-18, 2023-12-18
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
Daily Stand-ups: 2024-02-02, 2024-02-14
Zero Tolerance: 2024-02-05, 2024-02-05
Backlog Refinement: 2024-02-05, 2024-02-05
Zero Tolerance: 2024-02-12, 2024-02-12
Backlog Refinement: 2024-02-12, 2024-02-12
Iteration Review: 2024-02-15, 2024-02-15
Iteration Retrospective: 2024-02-15, 2024-02-15
Iteration Planning: 2024-02-15, 2024-02-15

section Iteration 4
Daily Stand-ups: 2024-02-16, 2024-02-28
Zero Tolerance: 2024-02-19, 2024-02-19
Backlog Refinement: 2024-02-19, 2024-02-19
Zero Tolerance: 2024-02-26, 2024-02-26
Backlog Refinement: 2024-02-26, 2024-02-26
Iteration Review: 2024-02-29, 2024-02-29
Iteration Retrospective: 2024-02-29, 2024-02-15
Iteration Planning: 2024-02-29, 2024-02-29

section Iteration 5
Daily Stand-ups: 2024-03-01, 2024-03-13
Zero Tolerance: 2024-03-04, 2024-03-04
Backlog Refinement: 2024-03-04, 2024-03-04
Zero Tolerance: 2024-03-11, 2024-03-11
Backlog Refinement: 2024-03-11, 2024-03-11
Iteration Review: 2024-03-14, 2024-03-14
Iteration Retrospective: 2024-03-14, 2024-03-14
Iteration Planning: 2024-03-14, 2024-03-14

section Iteration 6
Daily Stand-ups: 2024-03-15, 2024-03-20
Zero Tolerance: 2024-03-19, 2024-03-19
Backlog Refinement: 2024-03-19, 2024-03-19
Iteration Review: 2024-03-21, 2024-03-21
Iteration Retrospective: 2024-03-21, 2024-03-21
Iteration Planning: 2024-03-21, 2024-03-21

section OKR Current End
OKR Retrospective: 2024-03-22, 2024-03-22

section OKR Next Start
OKR Scene Setting: 2024-03-18, 2024-03-18
OKR Creation: 2024-03-25, 2024-03-26
OKR Impact Planning: 2024-03-27, 2024-03-27
@endmermaid

## OKR Ceremonies

### OKR Scene Setting

**Goal:** Ensure team understands current strategies and the teams purpose in order to prepare for the next ceremony [OKR Creation](#okr-creation)

**Duration:** Maximum of 1 day. If you can finish sooner then do so.

**Agenda:**

- Exercise: Everyone gets 5 minutes to write down what they think the current strategic objectives of the organisation are.
- Reveal: Set the strategic scene of the organisation by relaying the current company strategy to the team.
- Confirm: The organisations strategic scene is understood as a collective.
- Exercise: Everyone gets 5 minutes to write down what they think the current technical objectives of the organisation are.
- Reveal: Set the strategic scene of the technology by relaying the current technical principles and objectives to the team.
- Confirm: The organisations technical principles and objectives is understood as a collective.
- Exercise: Team breakouts in 2-3 people with 5-10 minutes to write down what they think the teams mission statement is.
- Reveal: Every breakout relays their team mission statement.
- Confirm: The team mission statement is agreed as a collective.
- Exercise: Team breakouts in 2-3 with 5-10 minutes to write down what they think the teams tenets are.
- Reveal: Everyone relays their team tenets.
- Confirm: The teams tenets are agreed as a collective.
- Review the current [categories of concern](#categories-of-concern) and their current status in the context of their values and the strategic context. Ensure they still provide coverage of the teams concerns and that they are still relevant.
- Based on precision, understand if we are missing any categories of concern because we don't have them at all or if they simply have not been made available. Ensure that making these available is a priority for the OKR creation ceremony next. If they cannot be made available they will likely become an objective for the next OKR cycle.

#### Categories of Concern

The initial ideation process of OKRs could be quite an expansive place to find yourself in. You're going to need to be drowning in data as you make your decisions on what to focus on in the next OKR cycle otherwise you are just guessing. Below are a set of categories I suggest you walkthrough as part of your ideation ceremony to prioritise what you need to do next. If you do find you are unable to prioritise or simply guessing at what you want to look at next, then I suggest first focussing on the "precision" concern below which should become a clear objective for the next OKR cycle.

|--|--|--|
| Category | Description | Examples |
|---|---|---|
| **Precision** | How easily can the team decide on which of the categories of concern we should focus on in the next OKR cycle. | Data availability for each of the below |
| **Performance** | How well are the products the team owns performing. | Conversion Ratios, Customer Satisfaction, Product Coverage |
| **Deliverability** | How fast are we able to deliver changes. | Lead Time, Deploys to Production per Day, Number of AB Tests Carried Out, Number of Experiments, Number of Rollbacks |
| **Cost** | How much are we spending to provide our products. | Cloud Costs, Third Party Contract Costs |
| **Reliability** | How reliable are the teams products. | Uptime, Volume of alerts |
| **Risk** | How secure and compliant are the teams products. | Number of Critical Vulnerabilities, Number of Risk Events |
| **Developer Experience** | How happy are the team developing. | Team Happiness, Code Complexity, Skills Coverage |
| **Integration** | How well the team makes its products data available to other teams. | Speed of Onboarding, Amount of Duplicated Data, Other Teams Satisfaction |

### OKR Creation

**Goal:** Create and confirm the objectives and key results for the next OKR cycle.

**Duration:** Maximum of 2 days. If you can finish sooner then do so.

**Agenda:**

- Review the OKR Ideation ceremony output
  - Ensure the company strategy understood
  - Ensure the technical strategy understood
  - Ensure the team mission agreed
  - Ensure the team tenets agreed
  - Ensure the categories of concern are understood and available
- Review precision as a collective, is any decision making data unavailable?
- Review performance as a collective, are our products performing well?
- Review deliverability as a collective, are we able to deliver changes quickly?
- Review cost as a collective, are we spending too much?
- Review reliability as a collective, are our products reliable?
- Review risk as a collective, are our products secure and compliant?
- Review developer experience as a collective, are the team happy developing?
- Review integration as a collective, are we making our products data available to other teams?
- Exercise: Team breakouts in 2-3 people with 5 minutes to write down what are the top three categories of concern.
- Reveal: Every breakout relays their categories of concern.
- Confirm: The team prioritises the top three categories of concern.
- Exercise: Team breakouts in 2-3 people with 15 minutes to write down what they think could be the team objectives.
- Reveal: Every breakout relays their objectives
- Confirm: The team prioritises the top four objectives.
- Exercise: Team breakouts in 2-3 people with 15 minutes to write down potential key results for the first objective.
- Reveal: Every breakout relays their key results.
- Action: Three key results are added to the first objective.
- Exercise: Team breakouts in 2-3 people with 15 minutes to write down potential key results for the second objective.
- Reveal: Every breakout relays their key results.
- Action: Three key results are added to the second objective.
- Exercise: Team breakouts in 2-3 people with 15 minutes to write down potential key results for the third objective.
- Reveal: Every breakout relays their key results.
- Action: Three key results are added to the third objective.
- Exercise: Team breakouts in 2-3 people with 15 minutes to write down potential key results for the fourth objective.
- Reveal: Every breakout relays their key results.
- Action: Three key results are added to the fourth objective.

**BREAK OVERNIGHT**

- Review the objectives and key results created the day before. Ensure there are no concerns.
- Action: Create objective zero and make sure the team understand its purpose.
- Exercise: Team breakouts in 2-3 people with 10 minutes to write down what they think should be the key results for objective zero.
- Reveal: Every breakout relays their key results.
- Action: Three key results are added to the objective zero.
- Exercise: Team breakouts in 2-3 people with 5 minutes to remove one of the four objectives initially planned.
- Reveal: Every breakout relays the objective they want to remove.
- Action: An objective is removed from the OKR cycle and replaced with objective zero.
- Action: The four objectives are added to the backlog with objective zero at the top.
- Action: The key results are added to the backlog objective zero and final refinement takes place before confirming.
- Action: The key results are added to the first backlog objective and final refinement takes place before confirming.
- Action: The key results are added to the second backlog objective and final refinement takes place before confirming.
- Action: The key results are added to the third backlog objective and final refinement takes place before confirming.
- Lastly, confirm the OKRs as a collective.
  
**Top Tip:** It is important to get the nights sleep in between formulating your ideas and then coming back to them. This is because you will likely have a different perspective on them the next day and you will be able to see if they are still as important as you thought they were.

### OKR Impact Planning

![OKR Plan]({{ site.baseurl }}/assets/2024-02-24-okr-agile-cycles/okr-plan.png)

**Goal:** Create initial hypotheses of how the team can move towards the key results of the objectives.

**Duration:** Maximum of 2 days. If you can finish sooner then do so.

**Frequency:**: Quarterly.

**Agenda:**

- Review the objectives and key results created in [OKR creation](#okr-creation).
- Exercise: Team breakouts in 2-3 people with 15 minutes to write down hypotheses that could impact the key results.
- Reveal: Every breakout relays their hypotheses.
- Confirm: The team hypotheses are prioritised as a collective. You will want at least three to satisfy the upcoming initial iterations.
- Action: Add the first hypotheses feature to the backlog with appropriate detail under the appropriate objective.
- Exercise: Team breakouts in 2-3 people with 15 minutes to write down work that could help deliver the first hypotheses.
- Reveal: Every breakout relays their work.
- Action: The team work items to deliver the first hypotheses are added as a collective to the backlog under the feature.
- Action: Add the second hypotheses feature to the backlog with appropriate detail under the appropriate objective.
- Exercise: Team breakouts in 2-3 people with 15 minutes to write down work that could help deliver the second hypotheses.
- Reveal: Every breakout relays their work.
- Action: The team work items to deliver the second hypotheses are added as a collective to the backlog under the feature.
- Action: Add the third hypotheses feature to the backlog with appropriate detail under the appropriate objective.
- Exercise: Team breakouts in 2-3 people with 15 minutes to write down work that could help deliver the third hypotheses.
- Reveal: Every breakout relays their work.
- Action: The team work items to deliver the third hypotheses are added as a collective to the backlog under the feature.
  
**BREAK OVERNIGHT**

- Review the work items added to the backlog and ensure they are still relevant and in the correct order. If they are not then change them. If a hypothesis is no longer relevant then remove it. If a new hypothesis has been created then add it to the backlog and repeat the exercises above.
- Exercise: Team refines the work items under the highest priority feature.
- Exercise: Team refines the work items under the second highest priority feature.
- Exercise: Team refines the work items under the third highest priority feature.
- Review the work items added to the backlog and ensure they are still relevant and in the correct order.

**Top Tip:** It is important to get the nights sleep in between formulating your ideas and then coming back to them. This is because you will likely have a different perspective on them the next day and you will be able to see if they are still as important as you thought they were.

### OKR Retrospective

**Goal:** Understand team member status and team efficiency in delivering the OKRs.

**Duration:** Maximum of 4 hours. If you can finish sooner then do so.

**Frequency:** Quarterly.

**Agenda:**

- Assess status of team with questionnaire.
- Review the team status feedback and understand any issues.
- Review team deliverability metrics like lead time for the last quarter.
- Exercise: Team writes down what well in the last OKR cycle.
- Exercise: Team writes down what didn't well in the last OKR cycle.
- Exercise: Team writes down ideas to improve future OKR cycles.
- Review and celebrate what went well.
- Review and understand what didn't go well.
- Review and understand the ideas to improve future OKR cycles, creating work items and adjusting future ceremonies where necessary.
- Celebrate the end of the OKR cycle and the start of the next.
  
**Top Tip:** Celebrate! You've just been working for an entire quarter, make sure you take the time to celebrate and socialise with the team and a job well done.

![Celebrate]({{ site.baseurl }}/assets/2024-02-24-okr-agile-cycles/celebrate.jpg)

## Iteration Ceremonies

### Daily Stand-ups

**Goal:** Update on current iteration work towards the goal and any blockers.

**Duration:** 15 minutes maximum.

**Frequency:** Daily.

**Agenda:**

- Reiterate the iteration goal which links to the OKRs that the team is working towards.
- Review the progress of work items from right to left on a kanban board.
- Identify any blockers and prioritise their removal.
- Ensure completed development work is prioritised for delivery and that every work item in any state has someone assigned to it.

**Top Tip:** Walking the board from right to left keeps the focus on the teams work to meet their goal and helps to keep focus away from individuals.

### Zero Tolerance

**Goal:** Identify critical errors, alerts and vulnerabilities that may cause the team not to meet their objective zero.

**Duration:** Maximum of 1 hour. If you can finish sooner then do so. If it is taking longer you likely need to revisit your objective zero or set an objective to improve the problems arising here. 

**Frequency:** Weekly.

**Agenda:**

- Review at a high level the ratio of requests to errors for every service.
- Identify those with the highest ratio of errors to requests and create a ticket if it breaks the thresholds set out in objective zero.
- Review at a high level the vulnerabilities for every service.
- Identify those with the most critical vulnerability create a ticket if it breaks the thresholds set out in objective zero.
- Review at a high level any outdated software for each service.
- Identify those with the shortest time to live and create a ticket if it breaks the thresholds set out in objective zero.

**Top Tip:** Using the key results set out in objective zero will make it very easy to prioritise what needs doing.

### Backlog Refinement

**Goal:** Ensuring the most valuable work to meet the OKRs is ready for the next iteration.

**Duration:** Maximum of 2 hours. If you can finish sooner then do so.

**Frequency:** Weekly.

**Agenda:**

- Ensure all zero tolerance tickets are refined and ready for the next iteration.
- Ensure all unplanned requests are reviewed and prioritised against the OKRs. If they do not align with the OKRs then they are not a priority and can be removed. If they are a priority then they should be refined.
- Confirm objectives and hypotheses are still in the correct order with regards to meeting team OKRs.
- Navigate the objectives and hypotheses as a team in priority order ensuring work is closed if all work is completed.
- Navigate the objectives and hypotheses as a team in priority order understanding what work is required to close each piece of work. This may mean either removing work items if now deemed less valuable or refining those that are not completed and are not yet ready to be worked on.

**Top Tip:** Using the key results set out in objectives will make it very easy to prioritise what needs doing and saying "no" to what doesn't meet those objectives.

![Focus]({{ site.baseurl }}/assets/2024-02-24-okr-agile-cycles/focus.jpg)

### Iteration Planning

**Goal:** Plan what work will be done in the next iteration to move closer to the key results of the objectives.

**Duration:** Maximum of 90 minutes. If you can finish sooner then do so.

**Frequency:** Fortnightly.

**Agenda:**

- Establish an iteration goal that links to the priority of the OKRs that the team is working towards.
- Capacity plan by understanding team absences, the team velocity and the amount of work that can be done in the next iteration.
- Move any active work items from the previous iteration into the current iteration.
- Review any of those not started from the previous iteration and understand if they are still valuable. If they are not then remove them.
- Add any objective zero work items to the current iteration.
- Navigate the objectives and hypotheses as a team in priority order and add relevant work items to meet the iteration goal.
- Confirm iteration workload in the context of the team capacity.
- Confirm sprint goal is understood and the workload will influence the key results of an objective as a result.

**Top Tip:** if you're backlog refinement meetings have been going well then planning should be easy!

### Iteration Review

**Goal:** Demonstrate progress made against the iteration goal and the OKRs.

**Duration:** Maximum of one hour. If you can finish sooner then do so.

**Frequency:** Fortnightly.

**Agenda:**

- Relay the iterations goal and how it links to the OKRs.
- Demonstrate the features delivered
- Demonstrate how the features delivered have moved the team closer to the OKRs with appropriate metrics.
- Gain feedback throughout from all stakeholders.

**Top Tip:** Invite appropriate stakeholders beforehand and ensure you demonstrate valuable features, not code.

### Iteration Retrospective

**Goal:** Understand team member status and team efficiency of delivering the iteration goal.

**Duration:** Maximum of 90 minutes. If you can finish sooner then do so.

**Frequency:** Fortnightly.

**Agenda:**

- Assess status of team with questionnaire.
- Review the team status feedback and understand any issues.
- Review team deliverability metrics like lead time for the last iteration.
- Exercise: Team writes down what well in the last iteration.
- Exercise: Team writes down what didn't well in the last iteration.
- Exercise: Team writes down ideas to improve future iterations.
- Review and celebrate what went well.
- Review and understand what didn't go well.
- Review and understand the ideas to improve future iterations, creating work items and adjusting future ceremonies where necessary.

**Top Tip:** From a leadership point of view treat retrospective actions as a high priority as it will immediately improve the team and demonstrate you are listening to their concerns.

## Stay Agile

All of the above are purely ideas, with the great thing about ideas is their ability to change and improve. You'll notice ceremonies like the backlog refinement and OKR creation repeat a number of agenda points that have happened likely quite recently in the previous ceremony. This is important because you should constantly revisit your priorities in the context of the here and now. What you believed to be true last week or last quarter is likely to have changed to the changes you have made as a team and the inevitable changes that have happened in the wider world. Could it be that having 80% of your most important objective being delivered now makes it the second most important objective? If so then you need to be able to change your priorities and reflect on this during your backlog refinement. In your OKR creation does your mission statement and team tenets still hold true? These would have a lower cadence of change but always take the time to go back over them and ensure they are still relevant in the world that you have changed since you last discussed them. If you have not completed an objective in a quarter, but it has improved, does it need to automatically carry over into the next quarter? Always revisit what is the most valuable thing you can be working on. It may often be that completing that objective is more advantageous than dropping it and starting something new, but always make that prioritisation call and understand why. It is far better to repeat your check-in of your current beliefs and constantly gather feedback than it is to not take that time and miss the opportunity to change and improve.

Every cycle, including the strategic OKR cycle has a retrospective. Much like you would do with your iteration retrospectives, ensure you are taking the time to reflect on how the OKR ceremonies are working for you and your team. If they are not working then change them. If they are working then keep them. The goal is to stay agile and to keep the team engaged and motivated. If you are not doing that then you are likely not doing it right, so make that change when you need to. Good luck and enjoy the journey!

![Flexible]({{ site.baseurl }}/assets/2024-02-24-okr-agile-cycles/flexible.jpg)