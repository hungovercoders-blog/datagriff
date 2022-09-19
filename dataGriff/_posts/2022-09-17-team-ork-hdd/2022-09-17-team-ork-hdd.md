Ki---
title: "Team-First, OKRs and Hypothesis Driven Development"
date: 2022-09-17

author: dataGriff
---

Below is a summary of the magic ingredients you can use to dramatically improve your organisations value and staff happiness.

- [Team First](#team-first)
- [OKRs](#okrs)
  - [Beer Team OKRs](#beer-team-okrs)
  - [Litter Team OKRs](#litter-team-okrs)
- [Hypothesis Driven Development](#hypothesis-driven-development)
- [Workflow Management Hierarchy](#workflow-management-hierarchy)
- [Monitor your Implementation](#monitor-your-implementation)

## Team First

I am a firm believer in a team-first approach to an organisation, instilling pride, enthusiasm and stability in an organisations staff should be seen as key to strategic success. Whilst there appears to be no clear evidence on a [teams stability outperforming a fluid team](https://www.scrum.org/resources/blog/depth-stable-or-fluid-teams-what-does-science-say), this is more due to a lack of the study itself than it actually being disproven.

There should be no doubting from a common sense perspective however that people who develop a close bond over time with a shared purpose will perform better. It will also minimize the amount of times that teams are outside of the high performing stage of [Tuckmans forming, storming, norming and performing stages of group development](https://en.wikipedia.org/wiki/Tuckman%27s_stages_of_group_development). Stable teams for me then are a winner, with the mantra "[bring your work to the people and not the people to work](https://medium.com/organize-agile/from-project-teams-to-stable-agile-teams-5934c271a8fc)" resonating with me and one you will hear me repeat often in the hope of assimilation.

![Borg]({{ site.baseurl }}/assets/2022-09-17-team-ork-hdd/borg.jpg)

Although not the purpose of this blog, appropriate team boundaries can be established utilising domain discovery methods such as [event storming](https://www.eventstorming.com/). Once business problem domains are identified they can be divided amongst your organisation using common sense around what business problems make the most sense to live closely together. The target implementation aiming to reduce handovers and ensuring teams can provided business value by reaching a customer independently, as well as resourcing domains accordingly based on their complexity. For further information on identifying a suitable team layout for your organisation please see resources on  [team topologies](https://teamtopologies.com/). **Top Tip:** Keep an eye out for cross-cutting platform teams that can support a lot of the repeated work across your value-based teams - you wouldn't want to repeat creation of authentication mechanisms across your organisation now would you?

## OKRs

OKRs stand for Objectives & Key Results. You may have other terms for them as they are ultimately a goal setting tool that I have found extremely inspiring. They allow a bottom-up as well as top-down approach to your organisations strategy. This allows teams close to the problem domains described above to utilise their knowledge under their own volition at the correct time to deliver value like only they know how. This is a high trust relationship between those running the organisation and the engineers they have employed, but one that should reap dividends if implemented successfully.  

A team **mission** should help understand objectives for the lifecycle of the team and should be fairly static. **Objectives** based on this mission should be agreed strategically with more senior members of the organisation and addressed about every 90 days. The **key results** then should be time-bound and an agreed method of how you will measure the success of your objectives. These objectives and key results should almost be unattainable, but realistic enough to be aspirational for the team as well as stretching them.

![MichaelSheen]({{ site.baseurl }}/assets/2022-09-17-team-ork-hdd/michael-sheen.jpg)

I recommend going to [what matters](https://www.whatmatters.com/) to learn more and also reading the [measure what matters book](https://www.amazon.co.uk/Measure-What-Matters-Simple-Drives/dp/024134848X) for more information.

As a quick example though...

### Beer Team OKRs

We have a established a team exclusively on making the hungovercoders drinking beer. Lets motivate them!

**Team Mission:** Ensure that the Hungovercoders Drink More Beer

**Objective:** Hungovercoders regularly go to the pub

**Key Results:**

- Five hungovercoders go to the pub at least once by the end of October 2022.
- Three hungovercoders go to the pub at least once a week by the end of November 2022.

### Litter Team OKRs

We have a established a team exclusively on ensuring the hungovercoders promote environmental concerns
. Lets motivate them!

**Team Mission:** Ensure that the Hungovercoders protect the environment 

**Objective:** Hungovercoders pickup litter

**Key Results:**

- Hungovercoders pickup 10 bags of rubbish a week by the end of September 2022.
- Hungovercoders local areas rate rubbish presence as reduced comparing September 2022 to November 2022.

As a reminder the OKRs are one of many frameworks for creating a measurable driving force for all of your teams. You may use something different but it is the one that I have identified with the most. The key thing to remember is parallelising your workforce to deliver multiple streams of value independently with clear indications of success is an immense force if you design it correctly.

## Hypothesis Driven Development

The final piece of the jigsaw and what makes the whole thing tick is [hypothesis driven development](https://www.thoughtworks.com/insights/articles/how-implement-hypothesis-driven-development)! We now encourage the teams to hypothesise how they can meet their objectives and influence their key results. This is a great empowerment tool for each team as they are essentially being recognised as the experts in their field with free reign to ideate and implement. This is a huge compliment and motivational factor you now get for free by setting yourself up in a high trust organisational manner. Imagine an army of motivated teams each with an area of the business to think up ideas and deliver value for, with clear agreed key results that were described up front.

These hypotheses can reflect themselves in sprints or iterations of the team which last about every 2 weeks. The goal being proving or failing to prove a hypotheses correct, much like the scientific method.

Some examples for the beer team might be:

- If we create a facebook group to encourage hungovercoders to socialise we will get three people to the pub in October!
- If we create a dedicated hungovercoders calendar app we will get two people going to the pub every week in November!

Some examples for the litter team might be:

- If we create a local neighbourhood whatsapp group to encourage hungovercoders and the community to pickup litter - we will pickup 5 bags each week in October!
- If we create a rate my litter app we will observe a reduction in litter presence between September 2022 and November 2022.

![Hypotheses]({{ site.baseurl }}/assets/2022-09-17-team-ork-hdd/hypothesis.jpg)

## Workflow Management Hierarchy

Constructing a suitable hierarchy of the above in a work management tool can also reap huge dividends by marrying up the strategic vision and actual work.

For example an epic can relate to an objective derived from a teams mission, a feature/sprint then represents a hypothesis, and then user stories are the work related to how you prove that hypothesis. With each code commit related to a story, you then have a complete audit change and hierarchical link from strategic objectives down through to the actual code that was worked on against it. This has a massive benefit of bringing together the business goals and the technical implementation, whereby there is no longer the traditional tooling or resulting organisational divide.

Below is an example implementation hierarchy, but know that your terminology of each components of the hierarchy may change based on your work management tool (e.g. you may regard as an Epic and a feature and so on). Ultimately though you should aim for the logical hierarchy described in this blog of the organisation > team > objective > hypothesis > work item > code commit to be visible and consistent across the business in one set of tooling.

![Hierarchy]({{ site.baseurl }}/assets/2022-09-17-team-ork-hdd/hierarchy.drawio.png)

## Monitor your Implementation

If you cannot get feedback from your teams on the success or failure of a hypotheses against a key result in around 2 weeks then you maybe you likely need to check if your objectives are too complex at this point, or more likely there may be an issue with your organisational setup if they cannot deliver independently. 

Either way keep dreaming the dream, you should be aiming for every team in your organisation to understand if they can impact business value every 2 weeks, with absolutely clear signals of how they are doing that along with full autonomy to do so. Go get 'em tigers!

![Tiger]({{ site.baseurl }}/assets/2022-09-17-team-ork-hdd/tiger.jpg)
