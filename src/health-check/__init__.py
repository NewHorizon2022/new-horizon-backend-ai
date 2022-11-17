import logging

import azure.functions as func
from shared_services import cognitive_services

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing Health Check')

    imagepath = req.params.get('path')

    if not imagepath:
        imagepath = 'https://newhorizonappstorage.blob.core.windows.net/demo-images/TBP_8461[1].jpg'
        
    try:
        # Call the cognitive services to check if it is up and running
        count = cognitive_services.count_people_in_photo(imagepath)
        return func.HttpResponse(f"Detected: {count}", status_code=200)
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
