# Cognitive services keys and endpoints
import os
import requests
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from shared_services.storage_services import upload_to_blob

KEY = '7261b8b4e5c24645a81a75db5def04c3'
ENDPOINT = 'https://new-horizon-compvision.cognitiveservices.azure.com'

def extract_license_plate(image_url, file_name, logger):
    # Create an Azure Computer Vision Client
    text_extraction_result = __extract_text_from_image(image_url, logger)
    lines = text_extraction_result['readResult']['pages'][0]['lines']

    for line in lines:
        logger.info(line['content'])
        # remove white spaces from string
        text = line['content'].replace(" ", "")
        if __validate_if_text_is_indian_license_plate(text, logger):
            __draw_shape_on_image(line['boundingBox'], image_url, file_name, logger)

# Extract text lines from an image using Azure Computer Vision Read API
def __extract_text_from_image(image_url, logger):
    endpoint = f'{ENDPOINT}/computervision/imageanalysis:analyze?api-version=2022-10-12-preview&features=Read&model-version=latest&language=en'
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': KEY
    }
    data = {
        'url': image_url
    }
    response = requests.post(endpoint, headers=headers, json=data)
    response.raise_for_status()
    analysis = response.json()
    logger.info(analysis)
    return analysis

def __validate_if_text_is_indian_license_plate(text, logger):
    logger.info(f'Validating if text is a valid Indian License Plate: {text}')
    if len(text) != 10:
        logger.info('License plate text is not 10 characters long')
        return False
    if not text[0:2].isalpha():
        logger.info('First two characters are not alphabets')
        return False
    if not text[2:4].isnumeric():
        logger.info('Next two characters are not numbers')
        return False
    if not text[4:6].isalpha():
        logger.info('Next two characters are not alphabets')
        return False
    if not text[6:10].isnumeric():
        logger.info('Last four characters are not numbers')
        return False
    logger.info('License plate text is valid')
    return True
    

def __draw_shape_on_image(bounding_box, image_url, file_name, logger, outline="blue"):
    logger.info(f'Drawing rectangle on image: {file_name}')

    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    draw = ImageDraw.Draw(image)

    draw.rectangle(
        [
            (bounding_box[0], bounding_box[1]),
            (bounding_box[-2], bounding_box[-1])
        ],
        outline=outline,
        width=5
    )

    image.save(file_name)