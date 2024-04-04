using Azure;
using Azure.AI.Translation.Text;


string key = "d7627....";
string endpoint = "https://ai102mlcservice1.cognitiveservices.azure.com/";

string languages = "da,pl";
string content = args[0];


string[] languageArray = languages.Split(',');

var credential = new AzureKeyCredential(key);


var client = new TextTranslationClient(
        credential: credential,
        endpoint: new Uri(endpoint));

var translations = await client.TranslateAsync(
        targetLanguages: languageArray,
        content: new string[] {content});


var actualTranslations = translations!.Value!.FirstOrDefault()!.Translations;

foreach(var translation in actualTranslations)
{
    System.Console.WriteLine($"{content} translated to {translation.To} is '{translation.Text}'");
}

