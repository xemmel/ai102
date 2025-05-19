


## templates

### V2 with long key

```json

"sku": {
                "name": "S0"
            },
            "kind": "AIServices",
            "properties": {
                "apiProperties": {},
                "customSubDomainName": "[parameters('accounts_mlcazureai_name')]",
                "networkAcls": {
                    "defaultAction": "Allow",
                    "virtualNetworkRules": [],
                    "ipRules": []
                },
                "allowProjectManagement": false,
                "publicNetworkAccess": "Enabled"
            }
        }
    }

```

### V1 with long keys

> Microsoft.CognitiveServices/accounts

```json

            "sku": {
                "name": "S0"
            },
            "kind": "CognitiveServices",
            "identity": {
                "type": "None"
            },
            "properties": {
                "apiProperties": {},
                "customSubDomainName": "[parameters('accounts_ai102mlcold_name')]",
                "networkAcls": {
                    "defaultAction": "Allow",
                    "virtualNetworkRules": [],
                    "ipRules": []
                },
                "allowProjectManagement": false,
                "publicNetworkAccess": "Enabled"
            }
        }

```


### Create CLI

```powershell

az cognitiveservices account list-kinds

az cognitiveservices account list-skus

```

```powershell

$serviceName = "ai102mlccli";
$location = "swedencentral";

$rgName = "rg-${serviceName}-remove";

az group create --name $rgName --location $location;


az cognitiveservices account create `
  --kind AIServices `
  --location  $location `
  --name $serviceName  `
  --resource-group $rgName `
  --custom-domain $serviceName `
  --sku S0
;

```


### Call OpenAI

```powershell


### Set body

$body = @"
{
        "messages": [
            {
                "role" : "system",
                "content" : "You are an angry chat bot"
            },
            {
                "role": "user",
                "content": "Who was the first us president?"
            }
        ]
}
"@;



### short key

$key = "7803f6b6993440ce8cd33bedfce3883f";
$baseUrl = "https://ai102mlccli.cognitiveservices.azure.com";
$modelName = "gpt-4.1";
$url = "${baseUrl}/openai/deployments/${modelName}/chat/completions?api-version=2025-01-01-preview";

curl $url -X POST -H "api-key:$key" -H "Content-Type:application/json" -d $body;


### Long key

$key = "3c5hmZ3ugWAiF0paBdM5zoH51wGawryBJVn5FjOJGPdt5QunA3YPJQQJ99BEACfhMk5XJ3w3AAAAACOGspt1";
$baseUrl = "https://mlcazureai.cognitiveservices.azure.com";
$modelName = "gpt-4.1";
$url = "${baseUrl}/openai/deployments/${modelName}/chat/completions?api-version=2025-01-01-preview";

curl $url -X POST -H "Authorization:Bearer $key" -H "Content-Type:application/json" -d $body;


$url = "${baseUrl}/openai/deployments/${modelName}/chat/completions?api-version=2025-01-01-preview";






```