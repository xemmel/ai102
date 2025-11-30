## Develop generative AI apps in Azure


### Python setup

```bash
sudo apt update && sudo apt upgrade -y

sudo apt install python3 python3-pip python3-venv -y

```


### Azure Setup

```bash

### install azure cli
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
az login --use-device-code


### Create Azure Resources

RGNAME="rg-ai4-remove"
FOUNDRYNAME="mlc4-ai"
LOCATION="swedencentral"


### Resource Group
az group create \
  --name $RGNAME \
  --location $LOCATION

### Foundry

az cognitiveservices account create \
   --name $FOUNDRYNAME \
   --resource-group $RGNAME \
   --location $LOCATION \
   --kind AIServices \
   --sku s0 \
   --custom-domain $FOUNDRYNAME

### Get Endpoint

ENDPOINT=$(az cognitiveservices account show \
--name $FOUNDRYNAME \
--resource-group $RGNAME \
| jq -r .properties.endpoint)


### Get Primary API key

APIKEY=$(az cognitiveservices account keys list \
--name $FOUNDRYNAME \
--resource-group $RGNAME \
| jq -r .key1)


### List deployments


az cognitiveservices account deployment list \
--name $FOUNDRYNAME \
--resource-group $RGNAME


### Create deployment

DEPLOYMENTNAME="gpt5"

export CUSTOM_OPENAI_DEPLOYMENT_NAME=$DEPLOYMENTNAME


az cognitiveservices account deployment create \
--name $FOUNDRYNAME \
--resource-group $RGNAME \
--deployment-name gpt5 \
--model-name gpt-5-chat \
--model-version "2025-08-07"  \
--model-format OpenAI \
--sku-capacity "50" \
--sku-name "GlobalStandard"


### Set env vars
export OPENAI_BASE_URL="${ENDPOINT}openai/v1"
export OPENAI_API_KEY=$APIKEY


### Remove

az group delete --name $RGNAME --yes

### Purge

az cognitiveservices account list-deleted -o json | jq '[.[] | {name: .name,location: .location,id: .id}]'



az cognitiveservices account purge --location $LOCATION --name $FOUNDRYNAME --resource-group $RGNAME


```


### Create virtual env and enter it

```bash

python3 -m venv azurelab

source azurelab/bin/activate

```

### Create small python app

```bash
mkdir smallapp
cd smallapp

cat<<EOF>>app.py
import sys

def main():
    try:
        arg = sys.argv[1]
        print(f"You said: '{arg}'")
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()
EOF

python app.py "Hello there, I'm a student"

cd -

```
> You said: 'Hello there, I'm a student'



### Azure API Key App

> Replace **abc**

```bash

mkdir azurekeyapp
cd azurekeyapp

pip install openai

FOUNDRYNAME="abc"
export OPENAI_BASE_URL="https://${FOUNDRYNAME}.openai.azure.com/openai/v1"
export OPENAI_API_KEY="abc"
export CUSTOM_DEPLOYMENT_NAME="abc"

cat<<EOF>>app.py
from openai import OpenAI
import sys
import os

def main():
    try:
        model_name = os.getenv("CUSTOM_DEPLOYMENT_NAME")
        client = OpenAI()
        question = sys.argv[1]
        response = client.responses.create(
            model = model_name,
            input = question
        )
        print(response.output_text)
    except Exception as ex:
         print(ex)

if __name__ == "__main__":
    main()
EOF

python app.py "Who was the first US president?"

### Notice that it's stateless

python app.py "Who was his wife?"


```

### Azure DefaultCredentials

```bash

cd -

mkdir azureapp
cd azureapp

pip install azure-identity 


```

```python
import sys
import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

def main():
    try:

        foundry_name = os.environ["CUSTOM_OPENAI_FOUNDRY_NAME"]
        message = sys.argv[1]
        model = os.environ["CUSTOM_OPENAI_DEPLOYMENT_NAME"]
        token_provider = get_bearer_token_provider(
            DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
        )
        url = f"https://{foundry_name}.openai.azure.com/openai/v1/"
        client = OpenAI(
            base_url = url,
            api_key = token_provider,
        )
        response = client.responses.create(
                    model=model,
                    input = message
                )
        print(response.output_text)
    except Exception as ex:
        print("Error: ",ex)

if __name__ == "__main__":
    main()

```

#### Create/Remove Role Assignment

```bash
MYUSERID=$(az ad signed-in-user show | jq .id -r)

 RESOURCEID=$(az cognitiveservices account show \
   --resource-group $RGNAME \
   --name $FOUNDRYNAME | jq .id -r)


### Add

az role assignment create \
   --assignee $MYUSERID \
   --scope $RESOURCEID \
   --role 53ca6127-db72-4b80-b1b0-d745d6d5456d

az role assignment delete \
   --assignee $MYUSERID \
   --scope $RESOURCEID \
   --role 53ca6127-db72-4b80-b1b0-d745d6d5456d



```

### Make conversation HTTP

```bash


```

### Make conversation code

```bash



```