DAY 4

AZURE Resources

   Man    (Access via internet, and security is always Entra) https://management.azure.com/
--------------------
  Data  <-------
         (Public Internet Access?)
                - Inbound traffic
                - Outbound traffic

         Web Application (API)
                - Inbound traffic (Will the API be accessable from Internet)
                       - NO INTERNET ACCESS    ->  Private Endpoint

                                 -> AI Service (ONLY ALLOW Traffic from a certain azure service (Pe1)
                                 -> Pe1 (Network interface)
                                           -> NI hookup to a Virtual Network (Subnet) (private ip address) (10.44.2.6)

                        When we're inside this VNET now, we can access on address (10.44.2.6)
                                 -> On the VNET a dns translation is setup https://ai102mlcdemo02.cognitiveservices.azure.com -> 10.44.2.6



                - Outbound traffic (When the API needs to communicate with "the outside world")
                         -> Instead of sending traffic to the internet, sent it to a Virtual Network instead


            
                  Web App -> https://ai102mlcdemo02.cognitiveservices.azure.com :-) (over the Internet)
                          Lock down AI Service (No internet access)
                          PE (Above)
                          (PE) Web app -> outbound traffic go to the same VNET as PE


Region/Subscription     
                          Hub and Spoke Model 

    Azure Resource ------->  VNET  (Rules) -> 




----------------

AZURE OPENAI
        Azure OPENAI Service 
             Create Model??

              


 	AI Services
        Azure OPENAI (ChatGPT, Dall-E, Ada)


AI Service    -> Endpoint, Key and "method" /vision/v3.2/read/analyze   GOOD TO GO







REST API / SDK













