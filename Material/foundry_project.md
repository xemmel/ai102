### Azure OpenAI Python

```bash

SUBSCRIPTIONID="9bc198aa-089c-4698-a7ef-8af058b48d90"
RGNAME="rg-ai-project-poc"
APPNAME="flow-project-poc"
LOCATION="swedencentral"


cd code
source ./devenv/bin/activate

pip install azure.ai.projects azure.identity



az group create \
  --name $RGNAME \
  --location $LOCATION \
  --subscription $SUBSCRIPTIONID


FOUNDRY=$(az cognitiveservices account create \
  --subscription $SUBSCRIPTIONID \
  --resource-group $RGNAME \
  --name $APPNAME \
  --custom-domain $APPNAME \
  --location $LOCATION \
  --kind AIServices \
  --sku S0 \
  --yes
)

PROJECT=$(az cognitiveservices account project create \
  --subscription $SUBSCRIPTIONID \
  --resource-group $RGNAME \
  --name $APPNAME \
  --project-name "${APPNAME}-project" \
  --location $LOCATION)


AZURE_PROJECT_ENDPOINT=$(echo $PROJECT | jq '.properties.endpoints."AI Foundry API"' -r)
export AZURE_PROJECT_ENDPOINT=$AZURE_PROJECT_ENDPOINT


### List models as csv

(
echo "name,version,format,sku,maxTokens,capabilities"
az cognitiveservices account list-models \
  --resource-group "$RGNAME" \
  --name "$APPNAME" \
| jq -r '
  .[]
  | [
      .name // "",
      .version // "",
      .format // "",
      .skuName // "",
      .maxTokens // "",
      (.capabilities // {} | keys | join("|"))
    ]
  | @csv
'
) | grep -i gpt



DEPLOYMENT=$(az cognitiveservices account deployment create \
   --subscription $SUBSCRIPTIONID \
   --resource-group $RGNAME \
   --name $APPNAME \
   --deployment-name common \
   --sku GlobalStandard \
   --capacity 500 \
   --model-format OpenAI \
   --model-name "gpt-5.4" \
   --model-version 2026-03-05
)






az resource list --resource-group $RGNAME --output table

```

### Python test client

```python

import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient



azure_project_endpoint = os.environ.get("AZURE_PROJECT_ENDPOINT")


credential = DefaultAzureCredential()
project = AIProjectClient(
        endpoint=azure_project_endpoint,
        credential=credential)

client = project.get_openai_client()
response = client.responses.create(
        model="common",
        input="First US president"
        )

print(f"Response output: {response.output_text}")

```

### Remove

```bash

az group delete   \
	--name $RGNAME   \
	--subscription $SUBSCRIPTIONID \
	--yes


az cognitiveservices account purge \
  --subscription $SUBSCRIPTIONID \
  --location $LOCATION \
  --name $APPNAME \
  --resource-group $RGNAME 
  

```