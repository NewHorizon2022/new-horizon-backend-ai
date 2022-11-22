# Add some imports
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials



def connect_to_azure_face_api():
    # Create an authenticated FaceClient.
    face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
    return face_client

# Count number of faces from a picture
def count_faces_from_picture(face_client, image_path):
    # Detect faces
    detected_faces = face_client.face.detect_with_stream(open(image
    _path, 'rb'), detection_model='detection_01')
    # Count number of faces
    number_of_faces = len(detected_faces)
    return number_of_faces
