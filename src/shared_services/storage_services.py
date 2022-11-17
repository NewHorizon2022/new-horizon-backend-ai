import os, uuid
import logging
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import azure.functions as func


# create a function that uploads to azure blob storage
def upload_to_blob(file_name):
    # connect to the storage account
    connect_str = os.getenv('AZUREWEBJOBSIMAGESSTORAGEACCOUNT')
    logging.info(f'Connection string: {connect_str}')

    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_name = "images"
    container_client = blob_service_client.get_container_client(container_name)

    logging.info('Opening file')
    with open(file_name, "rb") as data:
        logging.info(f'Uploading file {file_name}')
        blob_client = container_client.upload_blob(name=file_name, data=data, overwrite=True)
        logging.info('File uploaded')
