import logging
import azure.functions as func


def main(image: func.InputStream):
    return
    # logging.info(f"Python blob trigger function processed blob \n"
    #              f"Name: {image.name}\n"
    #              f"Blob Size: {image.length} bytes")
    
    # try:
    #     # Call the cognitive services to check if it is up and running
    #     count = cognitive_services.count_people_in_photo('https://newhorizonappstorage.blob.core.windows.net/demo-images/TBP_8461[1].jpg')
    #     logging.info(f"Detected: {count}", status_code=200)
    # except Exception as e:
    #     logging.error(f'Error: {str(e)}')
    
