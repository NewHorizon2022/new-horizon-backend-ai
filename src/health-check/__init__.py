import os
import logging
import azure.functions as func

poors_man_version = '0.0.1'

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing Health Check')

    cognitive_key                    = os.environ['COGNITIVE_SERVICES_KEY']
    cognitive_endpoint               = os.environ['COGNITIVE_SERVICES_ENDPOINT']
    appInsights_connection_string    = os.environ['APPINSIGHTS_CONNECTION_STRING']
    azure_webjob_storage             = os.environ['AZUREWEBJOBSSTORAGE']
    azure_webjob_images_storage      = os.environ['AZUREWEBJOBSIMAGESSTORAGEACCOUNT']

    if(cognitive_key and cognitive_endpoint and appInsights_connection_string and azure_webjob_storage and azure_webjob_images_storage):
        message = f'[V{poors_man_version}] Health Check OK'
        logging.warn(message)
        return func.HttpResponse(message)

    message = f'[V{poors_man_version}] Health Check ERROR'
    logging.error(message)
    return func.HttpResponse(message, status_code=500)
