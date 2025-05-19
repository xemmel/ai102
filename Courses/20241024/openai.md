### OpenAI

- Create a new *Azure AI Service* choose *sweden central* as Region
- open **ai.azure.com**

- Under *Management/All resources* find your newly create service
- Go to *Shared resources/Deployments*

- **+ Deploy model** -> *Deploy base model*
- Select *gtp-4o-mini* -> Name it *4omini* and leave all other properties and click **Deploy**


#### Call open AI

- In Azure Portal and your new service go to *Resource Management/Keys and Endpoint* and under **OpenAI** get:
   - Language API url
   - KEY 1

- In Postman: 


- Choose *POST*
- Use this url (change to your *Language API url*)
   https://mlcopenai102.openai.azure.com/openai/deployments/4omini/chat/completions?api-version=2024-08-01-preview

- In *Body* choose *JSON*

```json

{
   "messages" : [
       {
           "role" : "system",
           "content" : [
               {
                   "type" : "text",
                   "text" : "You can only answer with JSON and two elements: 'answer' and 'confidence'"
               }
           ]
       },
       {
           "role" : "user",
           "content" : [ {
               "type" : "text",
               "text" : "Who was the first us president"
           }
           ]
       },
       {
		"role": "assistant",
		"content": [
			{
				"type": "text",
				"text": "The first President of the United States was George Washington. He served from April 30, 1789, to March 4, 1797. Washington is often referred to as the \"Father of His Country\" for his leadership during the founding of the nation."
			}
		]
	},
           {
           "role" : "user",
           "content" : [ {
               "type" : "text",
               "text" : "Who was his wife"
           }
           ]
       }
   ]
}

```

- Set HEADER *api-key* and use the key fetched earlier


### Image upload sample

```json

{
   "messages" : [
          {
              "role" : "user",
              "content" : [
                  {
                  "type" : "image_url",
                  "image_url" : {
                      "url" : "https://www.osculati.com/SupplyImages/WF-0040/bandiera_svezia.jpg"
                  }
                  },
                  {
				"type": "text",
				"text": "Describe?"
			}
                  
              ]
          }
   ]
}

```


### Csharp example

dotnet new sln -o openaitester
cd openaitester
dotnet new console -o openaitester
cd openaitester

dotnet add package Azure.AI.OpenAI

code .

```csharp

using System.ClientModel;
using Azure;
using Azure.AI.OpenAI;
using OpenAI.Chat;


var credential = new ApiKeyCredential("7WR82m8iCBdHzxY2tWhUb8Lc2ueFdGfq7MMFnseBCbU7EzevYL4uJQQJ99AKACfhMk5XJ3w3AAAAACOGnTwK");

var client = new AzureOpenAIClient(
    endpoint: new Uri("https://mlcopenai102.openai.azure.com/"),
    credential: credential);

var chatClient = client.GetChatClient("4omini");

var messageSystem = ChatMessage.CreateSystemMessage("Answer in a rude manner");
var messageUser = ChatMessage.CreateUserMessage(args[0]);

var result = await chatClient.CompleteChatAsync(messageSystem,messageUser);
System.Console.WriteLine(result.Value.Content.First().Text);


```