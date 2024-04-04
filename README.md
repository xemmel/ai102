## AI 102

## Morten la Cour

## integration-it.com

lacour@gmail.com

#### Course labs

[mslearn-ai-services](https://github.com/MicrosoftLearning/mslearn-ai-services)

[mslearn-ai-vision](https://github.com/MicrosoftLearning/mslearn-ai-vision)

[mslearn-ai-language](https://github.com/MicrosoftLearning/mslearn-ai-language)

[mslearn-ai-document-intelligence](https://github.com/MicrosoftLearning/mslearn-ai-document-intelligence)

[mslearn-knowledge-mining](https://github.com/MicrosoftLearning/mslearn-knowledge-mining)

[mslearn-openai](https://github.com/MicrosoftLearning/mslearn-openai)

_Older_

[AI-102-AIEngineer - (Deprecated)](https://microsoftlearning.github.io/AI-102-AIEngineer/)

#### AI Service swagger

https://westeurope.dev.cognitive.microsoft.com/docs/services

#### API Docs

https://learn.microsoft.com/en-us/azure/ai-services/

### Prereq

#### Chocolatey.org

```powershell

Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

```

```powershell

choco install dotnet-sdk -y
choco install git -y
choco install vscode -y
choco install azure-cli -y


```

#### Winget

```powershell

 winget install Microsoft.AzureCLI --silent
 winget install Microsoft.VisualStudioCode --silent
 winget install Git.Git --silent
 winget install Microsoft.DotNet.SDK.8 --silent


```

[Back to top](#ai-102)

### Azure login

ai102student@integration-it.com

........ (Told by instructor)

REMEMBER: _Action Required_ **Ask Later** NOT _Next_

- portal.azure.com (Azure)
- entra.microsoft.com (Entra **AAD**)

[Back to top](#ai-102)

#### Get a token

```powershell

az account get-access-token --resource https://storage.azure.com/

```

### "Responsible" AI

#### Fairness

Not biased based on gender, ethnicity or others

#### Reliability & Safety

Working with selfdriving vehicle, or hospital systems

#### Privacy & Security

Data containing personal data should remain private

#### Inclusiveness

AI systems should empower everyone. Face recognizer: Not all people are nerds!

#### Transparency

AI systems should be understandable. Users should be made fully aware of the purpose of the system, how it works, and what limitations may be expected.

(We should always be able to explain why the model/system came to the conclusion)

#### Accountability

Designers and developers of AI-based solution should work within a framework of governance and organizational principles that ensure the solution meets ethical and legal standards that are clearly defined.

[Back to top](#ai-102)




#### Service Principal Manual get token

```

@clientId = 7d59f29f-58f9-4ae3-822f-4c1ce61a9367
@secret = MMW8....

POST https://login.microsoftonline.com/551c586d-a82d-4526-b186-d061ceaa589e/oauth2/v2.0/token

client_id={{clientId}}&client_secret={{secret}}&grant_type=client_credentials&scope=https://cognitiveservices.azure.com/.default





```

```powershell

$token = "...";
Invoke-WebRequest -Method Post -Uri "https://ai102mlcservice1.cognitiveservices.azure.com/contentmoderator/moderate/v1.0/ProcessText/Screen?autocorrect=true" -Headers @{"Authorization" = "Bearer $token";"Content-Type" = "text/plain";} -Body "Fuck you" | Select-Object COntent

```