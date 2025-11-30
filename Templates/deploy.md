## Deploy

```powershell

$appName = "mlcallaitypes2";
$location = "swedencentral";

$rgName = "rg-${appName}-remove";

az group create --name $rgName --location $location;

az deployment group create `
  --resource-group $rgName `
  --template-file .\Templates\aiservice.bicep `
  --parameters appName=$appName



az cognitiveservices account create `
  --kind AIServices `
  --location $location `
  --name "${appName}-cli2" `
  --resource-group $rgName `
  --sku S0 `
  --custom-domain "${appName}-cli2" `
  --verbose


az group delete --name $rgName --no-wait --yes;


```