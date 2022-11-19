# new-horizon-backend-ai
This is the microservice that call AI services

# To run this locally
```
cd src
python -m venv .venv
.\env\Scripts\activate
pip install -r requirements.txt
starter.sh
```

# To run this locally in a Docker container
```powershell
$storageAcountConnectionString = "Ex: DefaultEndpointsProtocol=htt... "
$appInsightsConnectionString = "InstrumentationKey=...;IngestionEndpoint=https://eastasia-..."
$image = "newhorizonappacr.azurecr.io/new-horizon-backend-ai:latest"
$cognitiveServicesKey = "..."
$cognitiveServicesEndpoint = "https://....cognitiveservices.azure.com/"

docker build . -t $image;
docker run -p 8889:80 `
   -v $(pwd):/mnt/python-code `
   -e AZUREWEBJOBSSTORAGE=$storageAcountConnectionString `
   -e AZUREWEBJOBSIMAGESSTORAGEACCOUNT=$storageAcountConnectionString `
   -e APPLICATIONINSIGHTS_CONNECTION_STRING=$appInsightsConnectionString `
   -e COGNITIVE_SERVICES_KEY=$cognitiveServicesKey `
   -e COGNITIVE_SERVICES_ENDPOINT=$cognitiveServicesEndpoint `
   $image
```


# Create a mount volume in azure container apps

```
$containerAppName = "new-horizon-cont-backend-ai-app"
$resourceGroupName = "new-horizon-rg"
$storageAccountKey = ""


az containerapp env storage set `
  --access-mode ReadWrite `
  --azure-file-account-name "newhorizonstorage" `
  --azure-file-account-key $storageAccountKey `
  --azure-file-share-name "python-code" `
  --storage-name "newhorizonstorage" `
  --name "new-horizon-cont-environment" `
  --resource-group $resourceGroupName `
  --output table

  az containerapp show `
  --name $containerAppName `
  --resource-group "new-horizon-rg" `
  --output yaml > app.yaml
```

then you need to find and add the template

```
template:
   containers:
      ...
      volumeMounts:
      - volumeName: python-code-volume
        mountPath: /mnt/python-code
   ...
   volumes:
    - name: python-code-volume
      storageName: "newhorizonstorage"
      storageType: AzureFile
```


And apply
```
az containerapp update `
  --name $containerAppName `
  --resource-group $resourceGroupName `
  --yaml app.yaml `
  --output table
```