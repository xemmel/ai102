## Hello


### Create first AI App

```powershell

dotnet new console -o myapp

cd myapp

dotnet add package Azure.AI.Translation.Text
dotnet add package Azure.Identity

code .

### Add extension C# Dev Kit

```

### Program.cs

```csharp

using Azure;
using Azure.AI.Translation.Text;
using Azure.Identity;

string endpoint = "https://!!!!.cognitiveservices.azure.com/";

string sourceMessage = args[0];
string languages = "da";


var credential = new DefaultAzureCredential();


var client = new TextTranslationClient(credential: credential,endpoint: new Uri(endpoint));



var translations = await client.TranslateAsync(
        targetLanguages: new string[] {languages},
        content:  new string[] {sourceMessage});

foreach(TranslationText translation in translations.Value.FirstOrDefault()!.Translations)
{
    System.Console.WriteLine($"{sourceMessage} translated: {translation.Text}");
}



```

```powershell

dotnet run "Hello this is a test"

### Error -> Not authorized

```