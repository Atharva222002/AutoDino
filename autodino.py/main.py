import pyautogui
import time
from PIL import Image,ImageGrab
def hit(key):
    pyautogui.keyDown(key)
    return
def ifCollide(data):
    for i in range(500,518):
        for j in range(195,230):
             if data[i,j] < 100:
                hit('space')           
                return
    for i in range(486 ,505):
        for j in range(160,185):
            if data[i,j] < 100:
                hit('down')
                return
    return
if __name__=="__main__":
    print('Your Game will start in 3 seconds.')
    time.sleep(3)
    hit('space')
    while True:
        image=ImageGrab.grab().convert('L')
        data=image.load()
        ifCollide(data)
