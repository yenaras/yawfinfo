#!/usr/bin/env python3
from mss import mss
import mss.tools
import numpy as np
import pytesseract
import cv2
# import time

pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

with mss.mss() as sct:
    monitor = sct.monitors[1]
    img = np.array(sct.grab(monitor), dtype=np.uint8)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(gray, (3, 3), 0)
    edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
    screenTesseractraw = pytesseract.image_to_string(
        gray,
        config="--psm 4 --tessdata-dir tessdata --user-words eng.user-words"
    ).split("\n")
    print(screenTesseractraw)
