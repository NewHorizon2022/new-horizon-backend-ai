import os
import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler, AzureEventHandler 
logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)
logger.addHandler(AzureLogHandler())
logger.setLevel(logging.INFO)

from urllib import request
from bottle import route, run, template, request
from process_image import process_image
from health_check import health_check
from shared_services import cognitive_services, license_plate_processing

@route('/api/process-image')
def index():
    url = request.query.filepath
    logger.info(f'Processing Process Image: {url}')
    output = process_image.process_image(url, logger)
    return output

@route('/api/health-check')
def health_endpoint():
    return health_check.health_check(logger)

@route('/api/find_license_plate')
def find_license_plate():
    url = request.query.filepath
    file_name = os.path.basename(url)
    logger.info(f'Processing Process Image: {url}')
    output = license_plate_processing.extract_license_plate(url, file_name, logger)
    return output

if __name__ == "__main__":
    run(host='0.0.0.0', port=80, debug=True, reloader=True)
