import pyautogui
import time
# gives us time to get situated in the game
for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

print('down')
pyautogui.keyDown('up')
pyautogui.keyDown('right')
time.sleep(10)
print('up')
pyautogui.keyUp('up')
pyautogui.keyUp('right')


