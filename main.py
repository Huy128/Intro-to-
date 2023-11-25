print('hello')

from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

import cv2
import time

import sys
from Adafruit_IO import MQTTClient
from Adafruit_IO import *

import pyttsx3

cam = cv2.VideoCapture(0)

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_Model.h5", compile=False)

def image_capture():
    ret,frame = cam.read()
    cv2.imwrite ("pic_test.png",frame)

def image_detector():
    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open("pic_test.png").convert("RGB")

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    # Get 1D array
    output = prediction[0]
    # Assign default value for max confidence
    max_index = 0
    max_confidence = output[0]
    # Find the maximum confidence and its index
    for i in range(1, len(output)):
        if max_confidence < output[i]:
            max_confidence = output[i]
            max_index = i
    print(max_index, max_confidence)

    file = open("labels.txt", encoding="utf8")
    data = file.read().split("\n")
    print("AI Result: ", data[max_index])
    client.publish('Face Mask check', data[max_index])

    if (data[max_index] == "No face mask"):
        engine = pyttsx3.init()
        engine.say("please wear a face mask")
        engine.runAndWait()
    elif (data[max_index] == "With face mask"):
        engine = pyttsx3.init()
        engine.say("you are pass, please come in")
        engine.runAndWait()

client = MQTTClient("Dungpq1401", "aio_cPsp36PRLRvA45KHV7I1FnSfW1MF")
client.connect()
client.loop_background()
while True:
    time.sleep(5)
    image_capture()
    image_detector()