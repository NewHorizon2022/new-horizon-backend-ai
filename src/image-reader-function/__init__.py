import logging
import azure.functions as func


def main(image: func.InputStream):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {image.name}\n"
                 f"Blob Size: {image.length} bytes")
