# new-horizon-backend-ai
This is the microservice that call AI services

# To run this locally in a Docker container
```powershell
$e = "<storage account url. Ex: DefaultEndpointsProtocol=htt... >"
docker build . -t image-reader-function; docker run -p 8889:80 `
   -e AZUREWEBJOBSSTORAGE=$s `
   -e AzureWebJobsImagesStorageAccount=$s `
   image-reader-function
```