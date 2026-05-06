## Azure AI Agent

```bash

RGNAME="rg-ai104-remove"
APPNAME="ai104mlc"
LOCATION="swedencentral"
SUBSCRIPTIONID="9bc198aa-089c-4698-a7ef-8af058b48d90"

PROJECTNAME="${APPNAME}-project"

az group create \
  --subscription $SUBSCRIPTIONID \
  --name $RGNAME \
  --location $LOCATION


ACCOUNT=$(az cognitiveservices account create \
  --subscription $SUBSCRIPTIONID \
  --resource-group $RGNAME \
  --name $APPNAME \
  --location $LOCATION \
  --kind AIServices \
  --sku S0 \
  --custom-domain $APPNAME \
  --yes
)  

PROJECT=$(az cognitiveservices account project create \
  --subscription $SUBSCRIPTIONID \
  --resource-group $RGNAME \
  --name $APPNAME \
  --project-name $PROJECTNAME \
  --location $LOCATION
)


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



### List agents

az cognitiveservices agent list \
   --subscription $SUBSCRIPTIONID \
   --account-name $APPNAME \
   --project-name $PROJECTNAME


AZURE_PROJECT_ENDPOINT=$(echo $PROJECT | jq '.properties.endpoints."AI Foundry API"' -r)
echo $AZURE_PROJECT_ENDPOINT

APITOKEN=$(az cognitiveservices account keys list --subscription $SUBSCRIPTIONID --resource-group $RGNAME --name $APPNAME  | jq .key1 -r)

AGENTNAME="flowgrait"
AGENTVERSION="1"
APIVERSION="2025-11-15-preview"




URL="https://${APPNAME}.services.ai.azure.com/api/projects/${PROJECTNAME}/openai/responses?api-version=${APIVERSION}"


QUESTION="hello"
BODY=$(cat <<EOF
{
  "input" : [
	{
		"role" : "user",
		"content" : "${QUESTION}"
	}
  ],
  "agent_reference": {
     "name" : "${AGENTNAME}",
	 "version" : "${AGENTVERSION}",
	 "type" : "agent_reference"
  }
}
EOF
)


RESPONSE=$(curl $URL \
  -d "$BODY" \
  -H "Authorization: Bearer $APITOKEN" \
  -H "Content-Type: application/json")


echo "$RESPONSE" | 
	jq -r '.output[] | 
	select(.type == "message") | 
	.content[] | 
	select(.type == "output_text") | 
	.text'




az group delete \
   --subscription $SUBSCRIPTIONID \
   --name $RGNAME \
   --yes &


az cognitiveservices account purge \
      --subscription $SUBSCRIPTIONID \
	  --resource-group $RGNAME \
	  --name $APPNAME \
	  --location $LOCATION




```