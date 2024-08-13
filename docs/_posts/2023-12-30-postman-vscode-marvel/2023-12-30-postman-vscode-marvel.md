---
title: "Creating postman collection for Marvel API in VS Code"
date: 2023-12-30
author: dataGriff
description: Creating postman collection for Marvel API in VS Code
image:
  path: /assets/2023-12-30-postman-vscode-marvel/link.png
tags: Postman VSCode API
---

I am way behind on my blogging given tis the season to be hungover and not coding... Below describes how to create a simple postman collection using the super [Marvel API](https://developer.marvel.com/){:target="\_blank"} leveraging environments and variables using the [postman VS Code extension](https://marketplace.visualstudio.com/items?itemName=Postman.postman-for-vscode){:target="\_blank"}. This I thought would be a great opportunity for me to see how API endpoints get structured and documented for a public facing API. I then show how you can add some examples, descriptions and tests (using AI no less!) in the [Postman app](https://www.postman.com/downloads/){:target="\_blank"}. **dataGriff SMASH!**

- [Prerequisites](#prerequisites)
- [VS Code Extension](#vs-code-extension)
  - [Create a Postman Environment](#create-a-postman-environment)
  - [Create Postman Collection](#create-postman-collection)
  - [Create a Characters Request](#create-a-characters-request)
  - [Create a Character Request](#create-a-character-request)
  - [Documentation](#documentation)
- [Postman App](#postman-app)
  - [Add Descriptions](#add-descriptions)
  - [Add Example](#add-example)
  - [Add Tests (Using Postman AI)](#add-tests-using-postman-ai)
- [VS Code Extension Revisited](#vs-code-extension-revisited)

## Prerequisites

- [Postman Account](https://www.postman.com/){:target="\_blank"} - This will be so you can use postman and ensure your settings are synced between the application and the VS code extension.
- [Postman App](https://www.postman.com/downloads/){:target="\_blank"} - This will provide some more functionality over the VS code extension such as AI assistant for test generation.
- [VS Code](https://code.visualstudio.com/){:target="\_blank"} - This to leverage the postman VS code extension.
- [Postman Extension](https://marketplace.visualstudio.com/items?itemName=Postman.postman-for-vscode){:target="\_blank"} - This to VS code extension we will experiment with.
- [Marvel Account](https://developer.marvel.com/account){:target="\_blank"} - This is to get your own public and private keys so that you can experiment with the Marvel API.

## VS Code Extension

First we're going to kick the tyres of the postman VS code extension and see how far we can get. If you have installed VS code postman as per the pre-requisites you should see postman available on the left-hand side.

![VSCode Postman]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/vscode_postman.PNG)

You'll also notice postman commands in the command palette (CTRL+SHIFT+P).

![VSCode Palette]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/vscode_pallete.PNG)

### Create a Postman Environment

In the postman extension, select environments, click add and call it "Marvel".

![New Environment]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/environment_new.PNG)

Add two variables:

- **apikey**: This will be the public api key from your Marvel developer portal.
- **PRIVATE_API_KEY**: This will be the private api key from your Marvel developer portal.
  Set both of these to be of type secret.

![Environment Keys]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/environment_keys.PNG)

Add another two variables:

- **hash**: This wll store the dynamically generated hash of the public key, the private key and the timestamp as per the marvel documentation to authenticate. Set this variable to be secret.
- **base_url**- This will hold the base url **"https://gateway.marvel.com:443/v1/public"** of the marvel API so we don't have to repeat it in our requests.

![Environment Keys]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/environment_variables.PNG)

### Create Postman Collection

In the postman extension, select collections, click add and call it "Marvel".

![New Collection]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/collection_new.PNG)

Give the collection a description.

![Collection Description]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/collection_description.PNG)

Ensure the collection is set to use the "Marvel" environment. This will ensure all the variables we have set will be inherited into this collection.

![Collection Environment]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/collection_environment.PNG)

Set the authorisation of the collection to use API Key with the key named apikey, the value to be the {{apikey}} which we have already set in the environment, and finally add this to the query params.

![Collection Auth]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/collection_auth.PNG)

Create a pre-request script that will generate a hash for us based on the public api key, the private api key and the built-in timestamp of the request. This will then set the Marvel environment has variable to be that hash at the point of request. This is a requirement to authenticate with the Marvel API.

Here is the script:

```javascript
const public1 = pm.environment.replaceIn("{{apikey}}"),
  private1 = pm.environment.replaceIn("{{PRIVATE_API_KEY}}"),
  time = pm.environment.replaceIn("{{$timestamp}}"),
  hash = CryptoJS.MD5(time + private1 + public1).toString();

pm.environment.set("hash", hash);
```

This is what it looks like in postman:

![Collection PreRequest]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/collection_pre_request.PNG)

We're going to set one variable at the collection level and that will be for the character id so that we can easily set it for the single character endpoint URL when calling multiple instances of it later. I have gone for 1009351 which is... HULK SMASH!

![Collection Character Id]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/collection_char_id.PNG)

### Create a Characters Request

First create a folder for "Characters" under your Marvel collection. This will just make your collection a little bit neater and we would likely want to keep comics and stories requests separate for ease of use.

![Collection Folder]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/collection_folder.PNG)

Add a GET request with the URL being **{% raw %}{{base_url}}/characters?hash={{hash}}&ts={{$timestamp}}{% endraw %}**. This will inherit the base_url and hash variables from our environment whilst also leveraging the built-in timestamp variable. We can also add each of the params documented in the [characters API](https://developer.marvel.com/docs){:target="\_blank"} but not tick them so they're not used yet.

![Request Characters Example 1]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/request_characters_ex1.PNG)

The apikey is also added as a request parameter. This is because in the Authorization section we set "Inherit auth from parent" which in the collection we know is the apikey set as a request parameter.

![Request Auth]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/request_auth.PNG)

All of this this ensures that the hash is consistent with the public api key and the timestamp query parameters that constructs it, along with the private key.

You can also debug your requests by turning the Postman console on (CTRL+SHIFT+P).

![Request Toggle Console]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/request_toggle_console.PNG)

You can then see all the logs and statuses in the Postman console below the request.

![Request Console]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/request_console.PNG)

Now try another request with the nameStartsWith parameter set to "spider". You will see in the request response that only characters that begin with spider are returned.

![Request Characters Example 2]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/request_characters_ex2.PNG)

### Create a Character Request

Add a GET request with the URL being **{% raw %}{{base_url}}/characters/{{character_id}}?hash={{hash}}&ts={{$timestamp}}{% endraw %}**. This will again inherit everything from the environment and parent as before. The only difference is it has a "character_id" variable as part of the URL which will only return the hulk. Send the request and see the response is indeed the hulk!

![Request Character]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/request_character.PNG)

### Documentation

You can view documentation at the request level in the VS code extension, but you cannot edit things like query parameter descriptions.

![Request Documentation]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/request_documentation.PNG)

You can also view documentation at the collection level.

![Collection Documentation 1]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/collection_documentation.PNG)

This also allows you to pick a particular language for your API interactions too as a quick start for your application code...

![Collection Documentation 2]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/collection_documentation_1.PNG)

However as I couldn't add examples in the VS Code extension which allows for this feature to kick-in, this was the first reason for me to go back to the postman app. I also wanted to edit documentation at the query parameter description level so this again led me to venturing back into the Postman app. Fear not we will be back to see it all synced up in VS code but we'll need to go into the postman app for some documentation, examples and AI generated testing!

## Postman App

I was hoping I'd never have to leave VS code ever again, and in the main this is true. I found the below at least at this point were easier to achieve in the postman app. I'll definitely be keeping an eye on this in the future to see if I never do have to leave VS code...

### Add Descriptions

First I added descriptions to the characters API query parameters by taking them from the [Marvel API docs](https://developer.marvel.com/docs){:target="\_blank"}.

![Postman Variable Descriptions]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/postman_variables.PNG)

### Add Example

I then generated a request with "Spider as the first part of the name and simply said save this as an example. This is great for documentation and will allow me to generate language specific code Quick Starts! We'll look at this in VS code when we revisit the documentation in the last part of this post.

![Postman Example]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/postman_example.PNG)

### Add Tests (Using Postman AI)

While I was in the postman app I was distracted by tests and the "Postbot"... Could I yet again handover my lack of knowledge to AI to get me going??? Yes I could! I asked it to "Add tests to this request" and it generated four simple tests. The only one I had to edit to get them all to pass (4/4) was the description property as this was more often than not blank in the API response.

![Postman Tests]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/postman_tests.PNG)

```javascript
pm.test("Response status code is 200", function () {
  pm.expect(pm.response.code).to.equal(200);
});

pm.test("Content-Type header is application/json", function () {
  pm.expect(pm.response.headers.get("Content-Type")).to.include(
    "application/json",
  );
});

pm.test(
  "Results array is present and contains the expected number of elements",
  function () {
    const responseData = pm.response.json();

    pm.expect(responseData).to.have.property("data");
    pm.expect(responseData.data).to.have.property("results");
    pm.expect(responseData.data.results).to.be.an("array");
    pm.expect(responseData.data.results).to.have.lengthOf.at.least(1);
  },
);

pm.test(
  "Name and description in results array are non-empty strings",
  function () {
    const responseData = pm.response.json();

    pm.expect(responseData.data.results).to.be.an("array");
    responseData.data.results.forEach(function (result) {
      pm.expect(result.name)
        .to.be.a("string")
        .and.to.have.lengthOf.at.least(1, "Name should not be empty");
      //pm.expect(result.description).to.be.a('string').and.to.have.lengthOf.at.least(1, "Description should not be empty");
    });
  },
);
```

## VS Code Extension Revisited

When I now go back into the VS code extension I can see that the documentation has been added to the query parameters.

![VS Code Docs 1]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/vscode_docs_1.PNG)

I can also go to the collection documentation and get starter code for my example requests in a range of languages! Sweet.

![VS Code Docs 2]({{ site.baseurl }}/assets/2023-12-30-postman-vscode-marvel/vscode_docs_2.PNG)

This has been a great introduction for me into a well formed API and given me a lot of thought of how I can make my own hungovercoder APIs accessible and usable in the future.
