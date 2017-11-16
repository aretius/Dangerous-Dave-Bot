import numpy as np
from PIL import ImageGrab
import cv2
import time
#from pywin32 import win32gui, win32ui, win32con, win32api

def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return processed_img



def grab():
    last_time = time.time()
    while(True):
        # 800x600 windowed mode
        screen =  np.array(ImageGrab.grab(bbox=(0,80,630,385)))
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        #cv2.imshow('window', new_screen)
        #if cv2.waitKey(25) & 0xFF == ord('q'):
        #    cv2.destroyAllWindows()
        #    break
        return new_screen
#screen_record()



