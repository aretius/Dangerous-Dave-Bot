from win32 import win32api as wapi
import time

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'APS$/\\":
    keyList.append(char)
#str(unichr(97))
keyList.append(chr(17))
keyList.append(chr(37))
keyList.append(chr(38))
keyList.append(chr(39))
def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys

