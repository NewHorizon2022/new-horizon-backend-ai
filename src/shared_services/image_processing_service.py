import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
import logging
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType
from shared_services.storage_services import upload_to_blob

def getRectangle(faceDictionary):
    rect = faceDictionary.face_rectangle
    left = rect.left
    top = rect.top
    bottom = top + rect.height
    right = left + rect.width
    logging.info(f'left: {left}, top: {top}, bottom: {bottom}, right: {right}')
    return (left, top, right, bottom)

def process_image(detected_faces, image_url, file_name):
    if not detected_faces:
        raise Exception('No face detected from image {}'.format(image_url))
    # Download the image from the url
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))

    # For each face returned use the face rectangle and draw a box.
    print('Drawing rectangle around face... see popup for results.')
    draw = ImageDraw.Draw(img)
    for face in detected_faces:
        rectangle = getRectangle(face)
        draw.rounded_rectangle(rectangle, outline='blue', width=5)

    # Add the count of faces detected to the image
    fnt = ImageFont.truetype("sans-serif.ttf", 60)
    width, height = img.size
    draw.text((width / 2, height / 2), detected_faces.__len__(), font=fnt, fill=(107, 0, 255, 64))

    # Display the image in the users default image browser.
    logging.info(f'Saving {file_name}...')
    img.save(file_name)
    logging.info(f'{file_name} saved')

    logging.info('uploading to blob...')
    upload_to_blob(file_name)

    logging.info(f'deleting {file_name}...')
    os.remove(file_name)
    logging.info(f'dile deleted: {file_name}.')