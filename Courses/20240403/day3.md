Azure Resource
     -> Metrics (90 days for "free")
     -> Actitivy Log (Management Planes LOG) (Will NOT show you "number of calls") (30 days for "free")
     
     -> Application Log WILL NOT BE STORED!!!!!


Custom Logging:
   - Application Log NEEDS to be stored!!
   - Longer retention days than the default

Two issues with Log Analytics Workspace: (Retention is 2 years max)

    - $$$$$$$$$$$$$$$$$$$$ (potentially)
    - Can loose data on peak-times!!!!


Two products that can solve the 2 problems above:

   - Storage Account (blobs) -> Cheap, many years retention (BUT, Onstructured data)
   - Event Hub (good at receiving mil. of me/sec)
        -> Short Retention (7 days)
             -> Consumer has to go and read from the event hub themself, WITH their own timestamp


ALERTS -> Metrics, Logs -> Queries "Select all errors within the last 10 min" -> if threshold > 2
     -> Send Text messages, email

      
Action Group -> Collection of Emails, text message


ALERT (WHat should it alert on, how often should it run) -> Action Group
ALERTS
ALERTS





System Managed Identites 

DevOps IaC

Sleep

- Create Azure Service (MI)
- Assign a Role to the (MI)  -> Does not exist



System Managed Identity 

1-1 between an Azure Resource -> MI  (Controlled by MS)
If you delete the resource the MI (User ENTRA) is also deleted automatically
An Azure Resource can only have ONE System MI (default)


User MI

User MI IS a normal Azure Resource
There is a many-many relationship between User MI and Azure Resource
    -> The same User MI can be used for multiple Services ("Group")
    -> An Azure Resource can have many User Managed Identity applied to it (1)

(1) If you want to use the User Managed Identity then you need to supply a ClientId when getting an access token




https://ai102mlcdemo02.cognitiveservices.azure.com/


d293838296724f909fdf920bed5f92e8

https://media.istockphoto.com/id/1204438215/vector/stop-sign-flat-design.jpg?s=612x612&w=0&k=20&c=un3FcIvkTgndgsH0sncvSzqJIMxH2nx3ir4AgVRGdjw=


Public: 

https://ai102mlcdemo1.blob.core.windows.net/mypubliccontainer/mortenstext.png

Private:

https://ai102mlcdemo1.blob.core.windows.net/myprivatecontainer/mortenstext.png




Consuming Service (AI Service)

Provider Service (Storage Account)

1) Make the consumer MI -> "User" in Entra
2) Add proper role assignment to the provider service for the consumer "user" (MI)


/vision/v3.2/read/analyze
Ocp-apim-subscription-key: {{key}}

{"url":"...."}


HEADER Response:

Operation-Location: https://.....

GET Operation-Location
Ocp-apim-subscription-key: {{key}}

-> Get the result


portal.azure.com 


- Try with a image uploaded to a private container
    -> 400 

-> AI Service (Consumer) (Portal) -> Identity -> Status -> On (Save) -> Get the name of your AIService

-> Storage Account (Provider)
   -> Access Control (IAM)
      -> Give your AI Service the role (SuperUser) -> "Review+Assign x 2"

-> Give a couple of min. -> Call :-)


Managed Identities:

- MFA (Humans)
- Service Principal (Service Account) -> UID/PWD


-   Azure Service 
     

          Expose a Data Layer (Role Assignment)
          80-90% Other Azure Resources (In the same tenant/Entra/AAD)

          
          WebApp   -> AI Service

1) Create a Service Account (SP)

                        Role Assignment (SP allowed to comm. with Speech)

          WebApp (Storage ClientId, Secret) -> USe that for getting a token -> Use that token towards AI

Managed Identity (System, User)

---------------------


Consuming Azure Resource -> Enable Managed Identity -> Azure Resource will become a "user/sp" in Entra

WebApp1 -> "User" in Entra called WebApp1 (GUID)  -> Now we can apply role assignment to WebApp1

WebApp: ai102webappmlc













