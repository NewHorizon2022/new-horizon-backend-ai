import logging

import asyncio
import io
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
# To install this module, run:
# python -m pip install Pillow
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, QualityForRecognition


# Cognitive services keys and endpoints
KEY = os.environ['COGNITIVE_SERVICES_KEY']
ENDPOINT = "https://eastus.api.cognitive.microsoft.com"

# Create a function that counts how many people are in a photo, using Microsoft FACE API
def count_people_in_photo(image_url) -> int:
    # Create an authenticated FaceClient.
    face_clienst = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

    # Detect faces in the image that contains the single face
    single_face_image_url = image_url
    single_image_name = os.path.basename(single_face_image_url)
    detected_faces = face_client.face.detect_with_url(url=single_face_image_url, recognition_model='recognition_01', return_recognition_model=False, detection_model='detection_03')

    if not detected_faces:
        raise Exception('No face detected from image {}'.format(single_image_name))

    for face in detected_faces: 
        logging.info(f'Detected face ID from {single_image_name} : {face.face_id}')

    logging.info(f'Detected {detected_faces.__len__()} faces')
    return detected_faces.__len__()
