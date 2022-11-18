import json
import os
import logging
import azure.functions as func

from shared_services import cognitive_services, image_processing_service
from shared_services.storage_services import upload_to_blob

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing Process Image')

    file_path = req.params.get('filepath')

    if not file_path:
        file_path = 'https://newhorizonappstorage.blob.core.windows.net/demo-images/TBP_8461[1].jpg'

    try:
        
        file_name = os.path.basename(file_path)
        logging.info(f'requesting to process file {file_name} from {file_path}')
                
        logging.info('counting people...')
        detected_faces = cognitive_services.count_people_in_photo(file_path, file_name)
        logging.info(f"Detected: {detected_faces.__len__()} faces")

        logging.info('processing image...')
        image_processing_service.process_image(detected_faces, file_path, file_name)
        logging.info('image processed')
        
        # Build a return object
        return_object = {}
        return_object['file_name'] = file_name
        return_object['file_path'] = file_path
        return_object['detected_faces_count'] = detected_faces.__len__()
        # return_object['detected_faces'] = detected_faces.response.json()

        logging.info('dumping json...')
        return_json = json.dumps(return_object)
        logging.info('that is it!')
        return func.HttpResponse(return_json, status_code=200)
        
    except Exception as e:
        logging.error(f'Error: {str(e)}')
        return func.HttpResponse(f"Error {str(e)}", status_code=500)