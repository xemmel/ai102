https://github.com/xemmel/ai102


Azure  (MS public cloud offering)

Azure    ->    Entra (AAD)  (MS public indentity Provider offering)
O365, D365...3rd, own apps  -> Entra


SSO


portal.azure.com   (azure, entra!!)


entra -> entra.microsoft.com

Entra -> Authentication (proving who I am) -> Showing your password (OpenId Connect)

Azure -> Authorization  -> Role Assignment (what can the "user" authenticated in entra do in Azure)

-------------

     Subscription1   -> Entra ID tenant1 (domain), creditcard, displayName, Free!!
         - More sub than just env.
         - Subscriptions as a Resource Group container
        
     (policy,security)  Resource Groups  -> Logical container for Resources
                -> All resources in the same RG has the same life-cycle!
               
               Resource (WebApp, VM, Azure Sql Server, Storage, AI.....) ($$)
                   

RG, (Resources) -> Region/Location 

     RG1 (R1) -> Acti. logging
        re1 (R2)
        re2 (R3) 

West Europe!!!

Regions
      - Complicance!!
    
      - Latency

      - Available versions/resources

      - Pricing


Region Pairs
  All regions has a mutual "friend"

  Enable Geo Redun -> $$
    > 300 miles
    Same geopolical zone (EU)

    Secondary Region -> Read Access Only (sec. url)

Availability Zones

   Region  -> > 3 Data centers
     
      -> Own water, power supply
      -> Optical cables between them


  

         ApplcationX
             - WebApp
             - WebApi
             - DB/Storage  -> MariaDb -> PostGres


        ARM Templates (bicep)
            Template 1-1 Resource Group

        ARM template (3 resource)


--------------

Management Group
   Subscription (on pr. appl/env)
       RG
          Resources
             (sub-resource)


policies, security (role assignment -> who can do what)
tag (NOT inherit)


---------------

RESOURCE


         Management/Control Plane    (CRUD)     -> ALWAYS ACC Through internet

Single endpoint -> ARM Rest API (https://management.azure.com/)
   Always uses (OAuth2/OIDC)  Always needs a token from Entra
   Need the permission -> Role assignment

---------------------------------------------------
         (Data/App) Plane     -> Calling the api 

    -> Disable public access (no internet access) (inbound/outbound)
    -> "Allow anonymous","Resource specific Passwords" and/or Entra Role Assignment

    "password" -> api-key, password, token, cert
         -> we need to have a rotate strategy


    Storage Account: "password" -> Key -> build a "token"

    Door to a night club 


-----------------------------


https://management.azure.com/

portal
azure cli, azure powershell
SDK



-------------------------
Resource/RG naming

ResourceId:

RG  

RGId (globally unique)

/subscriptionid/rgName


Resources:

/subscriptionid/rgName/type/resourceName


/sub1/rg1/vm/vm1   :-)
/sub1/rg1/vm/vm1   :-(
/sub1/rg/disk/vm1  :-)

/sub2/rg1/vm/vm1  :-)

Each Resource Type can have their own more contrained RULES!!!!

falckdkappxstorage

falckdkappxstoragetest   
falckdkappxstoragestage
falckdkappxstorage









App/User   -> Authenticate Entra

                -> Always ask entra for a token!!
                               (token have a purpose -> 
        - audience
        - scopes
        - resource
        - resourceUri


When you have a token


 Call an api
  
    Header:     Authorization: Bearer token


Role Assignment: Owner on the subscription



Owner: A local windows server Admin that has sql server installed on it.


Role Assignment: (Door mans list)
   - Role (Owner, Reader, Contri) -> What can we do
   - Identity (user, group, service account) -> Who can do it
   - Scope (sub,rg,resource) -> Where can we do it


Door man: accept "password" at all?
    Storage Account default: mixed mode (Accept both "password" and entra tokens)



Storage Account
     Key -> SAS Token -> Access blob

Owner -> FULL ACCESS TO THE MANAGEMENT PLANE (Keys)



----------------------------------

Data Science -> 

3,2
6,9
4,2
8
6
9

   ML   ->     -> NUMBERS   
       Images -> Snakes, Turtles -> 1 model (vision 




      AI  -> 


--------------------------------------------

ML/AI

Cognitive Service -> AI Services


Umbrella Service: Multi-Service AI    (vision, text, speech, documents....)
                          Individual services

                                 Vision Service (TeamA)
                                 Speech Service (TeamB)



Azure AI Search (Search Engine (Elastic Search) -> Lucene engine))


Azure OpenAI Service ($$$$$)  -> Can trained ($$$$$)
      - Use Existing Azure ben. billing, security
    
      ChatGPT / Dall-E











                                 

















