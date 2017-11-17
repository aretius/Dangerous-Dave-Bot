import numpy as np
from PIL import ImageGrab
import cv2
import time
from give_input import jump,right,left,shoot
from keras.models import load_model
from get_keys import key_check

WIDTH = 80
HEIGHT = 60
LR = 1e-3
EPOCHS = 50
MODEL_NAME = 'first_model_weights_nvgg.hdf5'



def main():
    model = load_model(MODEL_NAME)
    #print(model.summary())
    last_time = time.time()
    
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
    paused = False
    while(True):
        if not paused:
            screen =  np.array(ImageGrab.grab(bbox=(0,80,630,385)))
            print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (80,60))
#            cv2.imshow('ok',screen)
            moves = list(np.around(model.predict([screen.reshape(-1,80,60,1)])[0]))
            print(moves)
            
            if moves == [1,0,0,0,0]:
                left()
            elif moves == [0,1,0,0,0]:
                jump()
            elif moves == [0,0,1,0,0]:
                right()
            elif moves == [0,0,0,1,0]:
                shoot()
        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(3)
            else:
                paused = True
                
main()
