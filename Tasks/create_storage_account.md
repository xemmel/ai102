## Create Storage Account

- Create Resource Group containing your initials

- Create **Storage Account** select existing *Resource Group*

- Give it a unique name and leave other properties (choose region if default is not satisfactory)

- Goto *Advanced* and enable **Allow enabling anonymous access on individual containers**

- *Review/Create* -> *Create*

- Create two containers 
  - mypubliccontainer (Blob (anonymous...))
  - myprivatecontainer (Private (no an.....))


- Upload a small text file to each container and get the *Blob Url*
      - Click on Blob/file -> Copy **URL**


- Do a HTTP GET on the *url* (browser, postman or powershell (curl/invoke-webrequest)) verify that you **can** access the blob in **mypubliccontainer** and **cannot** access the blob in **myprivatecontainer**


----------------------------

```powershell

### Get Access token

az account get-access-token --resource https://storage.azure.com/


$token = ".....";


### If using local Powershell

az login --use-device-code

$token = az account get-access-token --resource https://storage.azure.com/ | ConvertFrom-Json  | Select-Object -ExpandProperty accessToken

### Change storage account name, container and blob name

invoke-WebRequest -Method Get -Uri https://ai102mlcdemo1.blob.core.windows.net/myprivatecontainer/Sample.txt -Headers @{ "x-ms-version" = "2023-08-03"; "Authorization" = "Bearer $token" }

```

You should get this error:

This request is not authorized to perform this operation using this permission.

- Goto Storage Account in Azure Portal
-  *Access Control (IAM)* -> Add -> Add Role Assignment
    - Storage Blob Data Reader
      - Select Members -> find yourself
      - Review + Assign
      - Review + Assign

Wait up to 6 min.
