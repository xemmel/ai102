Invoke-WebRequest -Method Post -Uri "https://ai102mlcservice1.cognitiveservices.azure.com/contentmoderator/moderate/v1.0/ProcessText/Screen?autocorrect=true"



Custom Vision Modelling



Object Detection
   -> Upload image of car/bicy.  -> 

    (10 min. build) -> Training 

Image Classification
    -> One object pr. image

 A  (Large Falck car)
 B  (Small Falck car)
 C

Lab: -> 3 hour



------------------------


Precision -> 90%

100

50 -> dogs
50 -> cats

50 images was identified as dogs, but only 45% were dogs

Precision = (True positives) / ((True Pos) + False Pos)

If the model iden. 100 images as dogs, and 90 of them are actual dogs = 90%

90 / (90 + 10)


Recall -> 99%

100 images of dogs, and the model only identified 90 as dogs = 90%

(True Pos) / (True Pos + False Neg)

100 / (100 +10) = 






2019  -> "Celebrities"   / Landmarks   -> Removed from "the default"
    Apply for it



2024  -> Landmarks are partly back??

-> Elvis, Bill Gates   






  Entra (AAD) -> Created a Service Principal (Service Account) 
          -> New App Registration
                 -> Give it a name
                 -> Register

 A Service Principal has been created 
            (A Service Principal  -> Combination of App Registration AND Enterprise Application)
                    App Registration (the entity for authentication (username/password) (clientId/Secret))
                    Ent. Applicaton (the entity for Authorization in Azure  -> Use for Role Assignment)


             

Secret for my Service Account -> Put in a Key Vault

App1   -> SP   (key)
App2
App3


API Key -> Don't want to have the API key lying in the APPS!

-> Key Vault
-> Create a SP (clientId/Secret)
-> Store the Secret!!!!!!!! in the App
-> Give Role Assignment on the KeyVault (secret reader) to the SP


--------------------

Role Assignments directly on AI Services -> GA

-> SP (sometimes we DONT need a secret/password for the SP -> Passwordless)
-> Add a Role Assignment to the AI SERVICE (Translate executor) to that SP


 NO KEYS


 -> OAUTH2 Token (AAD/Entra)    ->   Authorization: Bearer Token    (Need Role Assignment on our Resource (AI))



Service Principal -> Service Account


Assign Roles to that SP


SP - > Secret!!!


KeyVault: 

   -  Certif    :-)
   -  Keys (Crypto)   :-)
   -  Secret (plain text, sql connection string, ftp password)  -> Encrypted at rest (*)




Web App   -> Env var (app settings) -> Encrypted at rest (*)


    - Secrets
           - Multi use
           - Centralizing
 

   Image describer:

   -> Eifel -> Steel tower
   -> Car  -> Car
   -> Falck  -> Car / Falck car!!


------------------

   Falck     F1/F2/F3 ->   