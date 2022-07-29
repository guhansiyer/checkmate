from time import sleep
from PIL import ImageGrab

i = 0
sleep(3)
print('Start')
sleep(3)
for j in range(36):
    ss = ImageGrab.grab(bbox=(265, 165, 1070, 973))
    ss.save("C:\\Users\\guhan\\Desktop\\autoscreenshot\\Move"+str(i)+".png")
    i = i + 1
    print('Next move')
    sleep(3)