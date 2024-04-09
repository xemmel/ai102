using Azure;
using Azure.AI.Translation.Text;
using Azure.Identity;


//string key = "d76276d90b774b71a5482d1c29ec8c81";
string endpoint = "https://ai102mlcservice1.cognitiveservices.azure.com/";

string languages = "da,pl";
string content = args[0];


string[] languageArray = languages.Split(',');

//var credential = new AzureKeyCredential(key);
var clicredential = new AzureCliCredential();
var spcredential = new ClientSecretCredential(
        clientId: "7d59f29f-58f9-4ae3-822f-4c1ce61a9367",
        tenantId: "551c586d-a82d-4526-b186-d061ceaa589e",
        clientSecret: "MMW....");

var credential = new ChainedTokenCredential(
        clicredential,
        spcredential);


var credential = new DefaultAzureCredential();



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

