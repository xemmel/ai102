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

