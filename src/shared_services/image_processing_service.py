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
from PIL import Image, ImageDraw
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

    # For each face returned use the face rectangle and draw a red box.
    print('Drawing rectangle around face... see popup for results.')
    draw = ImageDraw.Draw(img)
    for face in detected_faces:
        rectangle = getRectangle(face)
        draw.rounded_rectangle(rectangle, outline='green', width=5)

    # Display the image in the users default image browser.
    img.save(file_name)
    logging.info(f'{file_name} saved')

    logging.info('uploading to blob...')
    upload_to_blob(file_name)

    logging.info(f'deleting {file_name}...')
    os.remove(file_name)
    logging.info(f'dile deleted: {file_name}.')