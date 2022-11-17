import os
import logging
import azure.functions as func

from shared_services import cognitive_services, image_processing_service
from shared_services.storage_services import upload_to_blob

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing Health Check')

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
        logging.info('processing image...')
        
        return func.HttpResponse(f"Detected: {detected_faces}", status_code=200)
    except Exception as e:
        logging.error(f'Error: {str(e)}')
        return func.HttpResponse(f"Error {str(e)}", status_code=500)


    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')
    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )
