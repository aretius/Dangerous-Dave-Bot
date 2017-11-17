import numpy as np
from grab_screen import grab
import cv2
import time
from get_keys import key_check
import os


def keys_to_output(keys):
    '''
    Convert keys to a ...multi-hot... array

    [Left arrow, Up arrow ,Right Arror, Ctrl, Alt] boolean values.
    '''
    output = [0,0,0,0,0]
    
    if chr(37) in keys:
        output[0] = 1
    elif chr(38) in keys:
        output[1] = 1
    elif chr(39) in keys:
        output[2] = 1
    elif chr(17) in keys:
        output[3] = 1
    elif chr(18) in keys:
        output[4] = 1
    return output


file_name = 'training_data.npy'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name))
else:
    print('File does not exist, starting fresh!')
    training_data = []


def main():

    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
        
    while(True):
        # 800x600 windowed mode
        screen = grab()
        last_time = time.time()
        #screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        # resize to something a bit more acceptable for a CNN
        screen = cv2.resize(screen, (80,60))
        keys = key_check()
        output = keys_to_output(keys)
        print(output)
        training_data.append([screen,output])
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        if len(training_data) % 500 == 0:
            print(len(training_data))
            np.save(file_name,training_data)
main()
