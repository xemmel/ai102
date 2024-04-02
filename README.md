## AI 102
## Morten la Cour
## integration-it.com



lacour@gmail.com


https://microsoftlearning.github.io/AI-102-AIEngineer/



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