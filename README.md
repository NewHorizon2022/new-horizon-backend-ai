# new-horizon-backend-ai
This is the microservice that call AI services

# To run this locally in a Docker container
```powershell
$storageAcountConnectionString = "Ex: DefaultEndpointsProtocol=htt... "
$appInsightsConnectionString = "InstrumentationKey=...;IngestionEndpoint=https://eastasia-..."
docker build . -t image-reader-function; docker run -p 8889:80 `
   -e AZUREWEBJOBSSTORAGE=$storageAcountConnectionString `
   -e AzureWebJobsImagesStorageAccount=$storageAcountConnectionString `
   -e APPLICATIONINSIGHTS_CONNECTION_STRING=$appInsightsConnectionString
   image-reader-function
```