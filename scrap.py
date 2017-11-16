from PIL import ImageGrab
import cv2
import time
import numpy as np

while(true):
    screen =  np.array(ImageGrab.grab(bbox=(0,80,630,385)))
