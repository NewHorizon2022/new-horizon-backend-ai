import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# create a function that uploads to azure blob storage
def upload_to_blob(file_name, logger):
    # connect to the storage account
    connect_str = os.getenv('AZUREWEBJOBSIMAGESSTORAGEACCOUNT')
    logger.info(f'Connection string: {connect_str}')

    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_name = "images"
    container_client = blob_service_client.get_container_client(container_name)

    logger.info('Opening file')
    with open(file_name, "rb") as data:
        logger.info(f'Uploading file {file_name}')
        blob_client = container_client.upload_blob(name=file_name, data=data, overwrite=True)
        logger.info('File uploaded')
