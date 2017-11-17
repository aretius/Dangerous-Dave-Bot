import pyautogui
import time
# gives us time to get situated in the game

def jump():
    pyautogui.keyDown('up')
    #time.sleep(1)
    pyautogui.keyUp('up') 
def right():
    pyautogui.keyDown('right')
    time.sleep(0.25)
    pyautogui.keyUp('right')
def left():
    pyautogui.keyDown('left')
    time.sleep(0.5)
    pyautogui.keyUp('left')
def shoot():
    pyautogui.keyDown('ctrl')
    pyautogui.keyUp('ctrl')
