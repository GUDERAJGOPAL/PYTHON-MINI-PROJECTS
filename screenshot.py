#import virtualenv
#import pyautogui
import time
import pyautogui as py
def screenshorts():
    time.sleep(5)
    img=py.screenshot('project.png')
    img.show()
screenshorts()
