import pyautogui
import time
import sys
from datetime import datetime
pyautogui.FAILSAFE = False
numMin = None
screenWidth, screenHeight = pyautogui.size()
if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numMin = 5
else:
    numMin = int(sys.argv[1])
while(True):
    x=0
    while(x<numMin):
        time.sleep(60)
        x+=1
    for i in range(0,2):
        pyautogui.moveTo(0,i*4)
    pyautogui.moveTo(int(screenWidth/2),int(screenHeight/2))
    # for i in range(0,3):
    #     pyautogui.press("shift")
    print("Movement made at {}".format(datetime.now().time()))