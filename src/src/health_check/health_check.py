import os

poors_man_version = '0.0.2b'

def health_check(logger):
    logger.info('Processing Health Check')

    cognitive_key                    = os.environ['COGNITIVE_SERVICES_KEY']
    cognitive_endpoint               = os.environ['COGNITIVE_SERVICES_ENDPOINT']
    appInsights_connection_string    = os.environ['APPLICATIONINSIGHTS_CONNECTION_STRING']
    azure_webjob_storage             = os.environ['AZUREWEBJOBSSTORAGE']
    azure_webjob_images_storage      = os.environ['AZUREWEBJOBSIMAGESSTORAGEACCOUNT']

    missing_variable = False

    if not cognitive_key:
        logger.info(f'Missing 1 cognitive_key: {cognitive_key}')
        missing_variable = True
    if not cognitive_endpoint:
        logger.info(f'Missing 2 cognitive_endpoint: {cognitive_endpoint}')
        missing_variable = True
    if not appInsights_connection_string:
        logger.info(f'Missing 3 appInsights_connection_string: {appInsights_connection_string}')
        missing_variable = True
    if not azure_webjob_storage:
        logger.info(f'Missing 4 azure_webjob_storage: {azure_webjob_storage}')
        missing_variable = True
    if not azure_webjob_images_storage:
        logger.info(f'Missing 5 azure_webjob_images_storage: {azure_webjob_images_storage}')
        missing_variable = True

    if missing_variable:
        message = f'[V{poors_man_version}] Health Check ERROR'
        logger.error(message)
        return message

    # All variables are present
    message = 'environment variables:\n'
    for k, v in os.environ.items():
        message += f'{k}={v}\n'

    message = f'[V{poors_man_version}] Health Check OK!'
    logger.info(message)
    return message
