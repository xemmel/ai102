param appName string
param location string = resourceGroup().location

resource aiServiceOld 'Microsoft.CognitiveServices/accounts@2025-04-01-preview' = {
  name: '${appName}-old-nonet'
  location: location
  sku: {
    name: 'S0'
  }
  kind: 'CognitiveServices'
  properties: {
    customSubDomainName: '${appName}-old-nonet'
  }
}

resource aiServiceOldNet 'Microsoft.CognitiveServices/accounts@2025-04-01-preview' = {
  name: '${appName}-old-net'
  location: location
  sku: {
    name: 'S0'
  }
  kind: 'CognitiveServices'
  properties: {
    customSubDomainName: '${appName}-old-net'
    networkAcls:{ 
      defaultAction: 'Allow'
    }
  }
}


resource aiServiceNew 'Microsoft.CognitiveServices/accounts@2025-04-01-preview' = {
  name: '${appName}-new-nonet'
  location: location
  sku: {
    name: 'S0'
  }
  kind: 'AIServices'
  properties: {
    customSubDomainName: '${appName}-old-nonet'
  }
}

resource aiServiceNewNet 'Microsoft.CognitiveServices/accounts@2025-04-01-preview' = {
  name: '${appName}-new-net'
  location: location
  sku: {
    name: 'S0'
  }
  kind: 'AIServices'
  properties: {
    customSubDomainName: '${appName}-old-net'
    networkAcls:{ 
      defaultAction: 'Allow'
    }
  }
}
