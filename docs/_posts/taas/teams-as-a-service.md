# Team as a Service

It is more important than ever to provide teams the ability to deliver value independently of any other team. The idea of "autonomous teams" is not so that teams can "do what they like", but it is to allow them to own and ship code within a loosely governed framework.

A common problem with modern platform teams is that rather than focusing on scaling out the ability to deliver, they focus too closely on providing all the actual engineering methods to prevent bad practices that they have been burned with in the past. This is not a surprising behavior, but one that must be overcome to provide fast independent throughput for all the teams in your company. If not you will soon find a new bottleneck in a centralized platform team that engineers will become dependent on and utilize as a new source of frustration and excuse for poor delivery.
It may also mean that developers do not upskill in things like deployment pipelines, which along with security, should be a staple in any engineers arsenal. Centralizing the techniques behind deployment and security for example, whilst in the short-term may show some success, over time the lack of feedback to developers leaves them blind and unskilled in these areas.

The below sets out some overstretched "as-a-service" paradigms to provide a "team as a service" quickly and prioritizes the **ability over the method** for a team to deliver. The warranted fear of bad practices coming into play should be be counteracted with automated governance in the cloud platform tools of choice and a suite of templates that engineers can choose from if they wish.

The key take home from this is you want to scale out the delivery of code and value to all your teams within a well-governed estate. The best way proposed here to do this, is to create rules centrally that allow fast feedback and learning to engineers, whilst giving them the freedom for to create and deliver from any team at any time.

- [Team as a Service](#team-as-a-service)
  - [Starting a new team](#starting-a-new-team)
  - [Communication as a Service (CaaS)](#communication-as-a-service-caas)
    - [Email Group](#email-group)
    - [Message Medium Channels and Handles](#message-medium-channels-and-handles)
  - [Repositories as a Service (RaaS)](#repositories-as-a-service-raas)
    - [Work Management](#work-management)
    - [Knowledge](#knowledge)
    - [Code](#code)
  - [Environment as a Service (EaaS)](#environment-as-a-service-eaas)
    - [Boundary](#boundary)
    - [Namespaces](#namespaces)
  - [Deployment as a Service (DaaS)](#deployment-as-a-service-daas)
    - [Service Connections](#service-connections)
    - [Pipeline Templates](#pipeline-templates)
  - [Layers as a Service (LaaS)](#layers-as-a-service-laas)
    - [Active Directory](#active-directory)
    - [Networking](#networking)
  - [Governance as a Service (GaaS)](#governance-as-a-service-gaas)
    - [Tagging Policies](#tagging-policies)
    - [Security Policies](#security-policies)
    - [Naming Convention Policies](#naming-convention-policies)
    - [Compliant Policies](#compliant-policies)
    - [Auditing](#auditing)

## Starting a new team

Creating a new team should not happen that often if you follow the ideas over [products over projects](https://martinfowler.com/articles/products-over-projects.html) and [domain driven design](https://martinfowler.com/bliki/DomainDrivenDesign.html) to map teams to business value areas. These areas are currently beyond the scope of this post but if you still follow project-based teams, the following process will likely cause you more pain as you too frequently spin up new teams with no ownership over the previous projects outputs.
The services described below provided by a platform team are therefore for long-lived teams only. All they require is a team name, membership and remit. The steps below then are what the platform team should aim to provide as a priority in an automated fashion. The **{teamname}** provided should be consistent through all the services provided below.

## Communication as a Service (CaaS)

Communications are critical to the success of a team as everyone should know how to contact the team. Combined with searchable knowledge and codebase mentioned in [RaaS](#repositories-as-a-service-raas), the bottlenecks of identifying who to contact about something is reduced dramatically. Providing all this from the offset gives a team form, membership and reduces long-term pain for other colleagues trying to find them.

### Email Group

An email distribution group should be setup with the format {teamname}@{company}.com. All provided team members should be added.

### Message Medium Channels and Handles

Appropriate message channels should be setup for the team in the companies standard channel setup. For example:

- {teamname} - A private channel for team members only.
- {teamname}-support - A public channel colleagues to request assistance.
- {teamname}-production - A public channel to post alerts and releases for production.
- {teamname}-test - A public channel to post alerts and releases for test.

A suitable handle for the team should be setup such as @{teamname} with all team members added. 

## Repositories as a Service (RaaS)

Repositories refers to bases where teams can store materials related to their work. This can be code, documents, tickets and wikis. All this is critical for a teams independence and quick starting. All of these assets should be granted access to the team [active directory group that will have been setup](#active-directory)). It is important that all other engineers in the organization are also granted at least read only access or more likely contributor access from the offset as well to prevent the team being hidden.

### Work Management

An appropriate and independent work management tool should be provisioned for the team, such as an Azure Devops Team project. The team project being within the organization and being called {teamname}.
Tools like this have the advantage of the team being able to create a Team Homepage from the wiki in the form of a Team API, that if described correctly can be a powerful search optimization tool. All the tickets being in the one tool also focuses any team members and focuses stakeholder and product owners to request work in the correct place.
If the project level is not specific enough for the team, then the backlog in the work management tool at a minimum should contain the {teamname}.

### Knowledge

Teams should have immediate access to some wiki tool and likely a document store. Azure Devops wikis compliment work management well above and are searchable across an organization so knowledge is still attainable by other teams. One drive or google drive may compliment the wiki and again a dedicated {teamname} drive would be preferable.

### Code

A codebase that the {teamname} has access to should be provided. This may be the team being granted to create and contribute to git repos in an Azure Devops wiki, or being provided access to create contribute to git repos in github. Either way a team requires to store code and reference it from deployment as soon as possible in order to deliver value.

## Environment as a Service (EaaS)

Ideally a team should be given its own environment to deploy code into as independent and unobstructed from other teams as possible. Whereas there may be concerns here around costs, at least these can be clearly identified. Once any inefficiencies occur platform can work with the team or teams to reduce costs.

### Boundary

An environment boundary is a space that the team can have dominion and freedom to work within. This for example could be an Azure resource group or even an Azure subscription. The latter has benefits with regards to clear billing and an estate that the team can break up its own problem domains into multiple resource groups.

### Namespaces

Namespaces are assets that may or may not be provisioned in advance by a platform team. Namespaces are logical containers for storage or compute that multiple problem domains can deploy into. Examples of these could include:

- Azure Storage Accounts
- Azure Service Bus
- Azure SQL Server
- Azure Event Hub Namespace
- Azure Data Factory

These namespaces could be deployed by the platform or the new team depending on what is available from platform from the offset. However, if the platform team begins to understand team patterns and behavior based on the teams mission, it could be that an environment boundary is provided with all appropriate namespaces from the offset.
In most cases these namespaces are free until some specific asset is added to them, so providing these by default for all teams may not be a waste of time and save time in the future by having them already available to experiment with. Costs here being catered for either by the team boundary or appropriate tagging. Care here must be given to the scale of these resources, but making them all available in test environments as an example on a lower tier for discovery and testing may improve innovation and value.

## Deployment as a Service (DaaS)

Each team should have the ability to deploy as soon as possible. It is critical they can do this independently. Based on the environment boundary, and potential namespace assets already created, secure credentials to deploy and then any appropriate templates means teams can deploy quickly.

### Service Connections

A team should be provided with secure connections to deploy into their new environment. In Azure DevOps this would be service connections mapped to resource group or subscription. Having these mapped to a team subscription from the offset would again mean teams can deploy immediately using these credentials. As well as providing these connections from the offset platform should provide the service to automatically renew or alert the team when credentials may be expiring.

### Pipeline Templates

Teams should have the ability to produce their own templates, but ones already created for them would be preferable over developing their own. Good engineers immediately turn to Google to create any new code, platform should ensure that their knowledge and codebase is so readily available that engineers would utilize their code if applicable. Centralizing pipeline templates outside of the team may cause a large dependency on one team, therefore copying and pasting templates for reuse within the locality of a team may be preferable.

## Layers as a Service (LaaS)

It is important that teams remain secure and have the ability to manage their own security. Platform should focus on creating a framework to allow just that.

### Active Directory

A security group should be setup for the team simply called {teamname} and have all team members added. Appropriate senior engineers from the team should be able to apply this AD group to their environment only.

In Azure an Administrative Unit should be setup for the team {teamname}, separated by live and test. Any new AD groups that the team sets up for specific data stores should be added to this and the team allowed to manage membership access.

Any concerns around monitoring what is going on with regards to access should be handled by platform auditing of the entire security estate.

### Networking

Networking is a difficult skill and this should be provided as simply as possible by the platform team. This may mean a virtual network per team with documentation on how to deploy assets into this, or simply documentation on how to integrate resources into the platform networking setup. The idea is to plan up front the inevitability of a team requiring the need for a secure network. Being proactive solves this problem, makes the solution available and the team can utilize it immediately and deliver.

## Governance as a Service (GaaS)

None of the above can be achieved without governing rules held centrally to ensure the estate does not become "teams can do what they like". Governance is a critical service to all of the above and any failure of a team not to meet appropriate compliant rules, is a failure of the central governing body and not the local teams.

### Tagging Policies

Ownership of all assets should be clear for costs and responsibility of alerting. A policy should be in place at a minimum to check that a team tag exists on all resources that map to a centrally held list platform expects.

Other tags such as business cost centre and environments should also follow similar suit.

Any resource that does not meet the tagging policy should fail on deployment.

### Security Policies

Any mandatory rules around security should be applied centrally and monitored by the platform team. Depending on the approach these may be audited or denied by default. The goal here is giving the team the ability to deploy but within secure guidelines. Examples of secure policies may be HTTPS is required or storage must be behind virtual networks. Whatever the rules the goal is to apply these and give the ability to the teams to deliver, with feedback from these rules deepening their understanding and learning over time. If platform always provided the complete method, and abstracted it too much, engineers would never learn.

### Naming Convention Policies

Naming convention policies can easily be maintained centrally to allow teams to deploy but meet platform standards. Again the method of adherence does not need to be given, just the feedback that rules have not been follow and rectification must take place. All occurring without the need for cross-team co-ordination or feedback, as it is all automated.

### Compliant Policies

There may be company-wide policies required to be applied that engineers must follow. This could be region specific data storage rules. By applying these centrally and allowing engineers to deploy, they can again learn and deliver independently.

### Auditing

It is critical that the entire estate is audited for what changes are taking place. This should be specifically on high-level audits in the main such as any resources being deployed, remove or altered, along with any security memberships being added to, removed or altered. These logs should be kept as long as is required by company policy. This is critical to allow engineering freedom but holding them accountable.