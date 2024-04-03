- Remove the API Key from the header
- 401!!!


- Get an access token with the aiservice audience

```powershell

az account get-access-token --resource https://cognitiveservices.azure.com/

```

Header: 
   Authorization: Bearer token


**Does not have permission**

- AI Service -> Access Control (IAM) -> Give yourself this role assignment: *Cognitive Services Language Owner*

Wait 5-6 (maybe more) min.

Execute again :-)


 
