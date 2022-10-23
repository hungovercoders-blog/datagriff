---
title: "Hide all your Implementation Details"
date: 2022-10-23

author: dataGriff
---

No matter how much they beg, no matter how much they cry, never share with them your implementation detail.

- [What is implementation detail and why should I care?](#what-is-implementation-detail-and-why-should-i-care)
- [Where are the layers of implementation and abstraction?](#where-are-the-layers-of-implementation-and-abstraction)
  - [What is an API, Event and Data Product](#what-is-an-api-event-and-data-product)
  - [Version All the Things](#version-all-the-things)
- [Abstracting the What-Is with APIs](#abstracting-the-what-is-with-apis)
  - [Example API Implementation](#example-api-implementation)
- [Abstracting the What-Happened with Events](#abstracting-the-what-happened-with-events)
  - [Example Event Implementation](#example-event-implementation)
- [Abstracting the What-Was with Data Products](#abstracting-the-what-was-with-data-products)
  - [Example Data Product Implementation](#example-data-product-implementation)

## What is implementation detail and why should I care?

## Where are the layers of implementation and abstraction?

Each layer acts as a firewall to change gracefully at each implementation point and for consumers to change at their own cadence, the result is a more decoupled architecture.

### What is an API, Event and Data Product

### Version All the Things

But at some point we're inevitably going to change something in our abstraction layers? We can't foresee us creating the worlds most perfect APIs, events and data products in one hit can we?? No of course not. The cadence of the changes to these abstractions though should be far lower as they do not change when the internal implementations change. To cater for these breaking changes and allow consumer cadence of change to remain decoupled from the initial change, we use versioning. The application or insights layer will create new versions of APIs, events or data products whilst still maintaining the old one for a certain period. Consumers can then gracefully migrate off by an end of life date provided to them by the provider of the API, event or data product. This means we are temporally decoupled from changes between systems by using versioning as well as technically decoupled using the protection layers of API, event and data product.

## Abstracting the What-Is with APIs

Great source of [API resource naming standards](https://www.restapitutorial.com/lessons/restfulresourcenaming.html).

### Example API Implementation

## Abstracting the What-Happened with Events

### Example Event Implementation

## Abstracting the What-Was with Data Products

What about quick access to data... we must have engineers and analytics in the same team allowing a cohort of analysts to get insights early. Effort must be spent in creating data products or you will enter a long term dependency battle. Insights being available internally to the team by having the makeup of the team correct should counterbalance any concern about speed to insights, as the right people will have access, just not on a consumer-wide scale yet.



Frustrated analysts in a separate team waiting for data engineers to provide an entire data warehouse for your entire business will fail. The results will likely be engineers taking far too long to deliver any value due to the multiple domains they are trying to solve in one go, with analysts becoming frustrated and undoubtedly starting to make their own data domains directly from internal implementations. No one wins. Aligning data engineers with analysts within smaller domains first to allow insights within a team before data sharing with others is critical for the success of this decoupled architecture. Well thought out distributed data products from multiple domains can later become the source for a new consumer domain, that wil undoubtedly looks across multiple source domains to create a grander picture of your estate. Do not default to making a global data warehouse from the offset that covers a 360 view of your business. This is a massive project and far too slow for our modern agile needs. Distribute smaller data domains in parallel across multiple cross-functional teams to create insights within these spaces instantly, along then with considered published data products that have a slightly lower cadence compared to the internal team insights. Once these consumer facing data products are in place from multiple areas, then you have the abstracted building blocks to make decoupled data domains that look across the multiple domains of your business.

databricks can abstract awway [multiple formats](https://docs.databricks.com/external-data/index.html).

### Example Data Product Implementation

With the buzz around data mesh...