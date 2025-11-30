## Deploy

```powershell

$appName = "mlcallaitypes";
$location = "swedencentral";

$rgName = "rg-${appName}-remove";

az group create --name $rgName --location $location;

az deployment group create `
  --resource-group $rgName `
  --template-file .\Templates\aiservice.bicep `
  --parameters appName=$appName


az group delete --name $rgName --no-wait --yes;


```