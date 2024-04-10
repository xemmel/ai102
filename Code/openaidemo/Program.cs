
using Azure.AI.OpenAI;

string endpoint = "https://intitai-test-ai.openai.azure.com/";
string key = "b5.......";
string deployment = "chatdeployment";


var client = new OpenAIClient(endpoint: new Uri(endpoint), keyCredential: new Azure.AzureKeyCredential(key));


ChatCompletionsOptions chatCompletionsOptions = new ChatCompletionsOptions()
{
    Messages =
    {
        //new ChatRequestSystemMessage(systemMessage),
        new ChatRequestUserMessage(args[0]),
    },
    MaxTokens = 400,
    Temperature = 0.7f,
    DeploymentName = deployment
};


// Send request to Azure OpenAI model
ChatCompletions response = client.GetChatCompletions(chatCompletionsOptions);

// Print the response
string completion = response.Choices[0].Message.Content;
Console.WriteLine("Response: " + completion + "\n");



