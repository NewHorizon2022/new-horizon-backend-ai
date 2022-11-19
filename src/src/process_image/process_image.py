import os
import json

from shared_services import cognitive_services, image_processing_service

def process_image(file_path, logger):
    logger.info('Processing Process Image')

    if not file_path:    
        raise Exception('No file path provided')

    file_name = os.path.basename(file_path)
    logger.info(f'requesting to process file {file_name} from {file_path}')
            
    logger.info('counting people...')
    detected_faces = cognitive_services.count_people_in_photo(file_path, file_name, logger)
    logger.info(f"Detected: {detected_faces.__len__()} faces")

    logger.info('processing image...')
    image_processing_service.process_image(detected_faces, file_path, file_name, logger)
    logger.info('image processed')
    
    # Build a return object
    return_object = {}
    return_object['file_name'] = file_name
    return_object['file_path'] = file_path
    return_object['detected_faces_count'] = detected_faces.__len__()
    # return_object['detected_faces'] = detected_faces.response.json()

    logger.info('dumping json...')
    return_json = json.dumps(return_object)
    logger.info('that is it!')
    return return_json