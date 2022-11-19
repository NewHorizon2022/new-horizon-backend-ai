
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

@route('/api/process-image')
def index():
    url = request.query.filepath
    logger.info(f'Processing Process Image: {url}')
    output = process_image.process_image(url, logger)

    return output

@route('/api/health-check')
def health_endpoint():
    return health_check.health_check(logger)

run(host='0.0.0.0', reloader=True, port=80)
