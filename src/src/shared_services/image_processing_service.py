import os
import requests
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType
from shared_services.storage_services import upload_to_blob

def get_rectangle_from_face(faceDictionary, logger):
    rect = faceDictionary.face_rectangle
    left = rect.left
    top = rect.top
    bottom = top + rect.height
    right = left + rect.width
    logger.info(f'left: {left}, top: {top}, bottom: {bottom}, right: {right}')
    return (left, top, right, bottom)

def draw_rectangles_on_faces (detected_faces, image_url, file_name, logger):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    draw = ImageDraw.Draw(img)

    if detected_faces:
        # For each face returned use the face rectangle and draw a box.
        logger.info('Drawing rectangle around face... see popup for results.')
        for face in detected_faces:
            rectangle = get_rectangle_from_face(face, logger)
            draw.rounded_rectangle(rectangle, outline='blue', width=5)

    # Add the count of faces detected to the image
    width, height = img.size
    logger.info(f'image size: width: {width}, height: {height}')
    
    logger.info('loading font')
    try:
        fnt = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', int(height / 2))
    except:
        fnt = ImageFont.truetype("C:/Users/crgar/Downloads/KrutiDev040Bold/Krutidev_040_bold/Krutidev_040_bold.TTF", int(height / 2))
        
    logger.info(f'done loading font. Image size {img.size}. Font Size {fnt.size}')

    #draw.text((int(width / 2), int(height / 2)), str(detected_faces.__len__()), font=fnt, fill=(0, 255, 0, 64))
    logger.info('done drawing text')

    # Display the image in the users default image browser.
    logger.info(f'Saving {file_name}...')
    img.save(file_name)
    logger.info(f'{file_name} saved')

    logger.info('uploading to blob...')
    upload_to_blob(file_name, logger)

    logger.info(f'deleting {file_name}...')
    os.remove(file_name)
    logger.info(f'dile deleted: {file_name}.')


    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    draw = ImageDraw.Draw(img)#
    draw.shape()
    draw.rounded_rectangle(rectangle, outline, width=5)

    width, height = img.size
    logger.info(f'Image size: width: {width}, height: {height}')
    
    logger.info(f'Saving {file_name}...')
    img.save(file_name)
    logger.info(f'{file_name} saved')

    logger.info('uploading to blob...')
    upload_to_blob(file_name, logger)

    logger.info(f'deleting {file_name}...')
    os.remove(file_name)
    logger.info(f'dile deleted: {file_name}.')