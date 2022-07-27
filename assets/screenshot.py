from time import sleep
from PIL import ImageGrab
import keyboard as k

i = 0
while True:
    if k.is_pressed('a'):
        pic = ImageGrab.grab(bbox=(265, 165, 1070, 973))
        pic.save("C:\\Users\\guhan\\Desktop\\autoscreenshot\\Move"+str(i)+".png")
        i = i + 1
        sleep(1)