import io
import os
from google.cloud import vision_v1p3beta1 as vision
from datetime import datetime
import cv2

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'My First Project-c73adf32e5ef.json'
path = '10.jpeg'


def recognise_license_plate(img_path):
    client = vision.ImageAnnotatorClient()
    start_time = datetime.now()

    with io.open(img_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    for text in texts:
        if len(text.description) == 7:
            license_plate = text.description
            print('License Plate {}'.format(license_plate))
            print('Total Time :{}'.format(datetime.now() - start_time))


recognise_license_plate(path)
