#!/usr/bin/env python3
from mss import mss
import mss.tools
import numpy as np
import pytesseract
import cv2
import re
import imutils

pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
tes_con = (
    r'--psm 7 --tessdata-dir tessdata')


def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def resize(image):
    return imutils.resize(image, width=200)


def remove_noise(image):
    return cv2.GaussianBlur(image, (3, 3), 0)


def threshold(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


def clean(text):
    return re.sub(r'[^\w ]+', ' ', text)


dict_list = [
    {"top": 430, "left": 2420, "width": 220, "height": 35},
    {"top": 430, "left": 2655, "width": 220, "height": 35},
    {"top": 430, "left": 2888, "width": 220, "height": 35},
    {"top": 430, "left": 3120, "width": 220, "height": 35}
]
data = []


def relic_drops():
    with mss.mss() as sct:
        for i in dict_list:
            img = np.array(sct.grab(i))
            img = get_grayscale(img)
            img = resize(img)
            img = remove_noise(img)
            img = threshold(img)
            raw_data = pytesseract.image_to_string(
                img, config=tes_con)
            clean_data = clean(raw_data)
            data.append(clean_data.strip())
    return data
