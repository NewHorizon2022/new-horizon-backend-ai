# new-horizon-backend-ai
This is the microservice that call AI services

# To run this locally in a Docker container
```powershell
$storageAcountConnectionString = "Ex: DefaultEndpointsProtocol=htt... "
$appInsightsConnectionString = "InstrumentationKey=...;IngestionEndpoint=https://eastasia-..."
$image = "newhorizonappacr.azurecr.io/new-horizon-backend-ai:latest"
docker build . -t $image; 
docker run -p 8889:80 `
   -e AZUREWEBJOBSSTORAGE=$storageAcountConnectionString `
   -e AZUREWEBJOBSIMAGESSTORAGEACCOUNT=$storageAcountConnectionString `
   -e APPLICATIONINSIGHTS_CONNECTION_STRING=$appInsightsConnectionString `
   -e COGNITIVE_SERVICES_KEY=... `
   $image
```