'''import files as files
from gtts import gTTS'''
import os
import pyautogui
import sys


SS_path = "C:/Users"
myScreenshot = "screenshot"
screenshot = 0

#change values based off the data from the text box code
begin_x = 245
begin_y = 17
area_of_x = 1675
area_of_y = 790

while True:
    try: 
        print("Taking a screenshot...")
        screenshot = pyautogui.screenshot(SS_path + myScreenshot + ".png",section = (begin_x, begin_y, area_of_x, area_of_y))
    except Exception as e:
        print(e)
    print("Screenshot taken, parameteres of the file are: " + str(screenshot))

    file_path = os.path.join(SS_path, '*')

"""import pyautogui
import sys
import os

screenshotName = "screenshot"
path = "C:/Users"

x_start_point = 245
y_start_point = 70
x_area = 1675
y_area = 790

screenshots = 0
while True:
    try:
        print("Taking a screenshot...")
        screenshots = pyautogui.screenshot(path + screenshotName + ".png",region = (x_start_point, y_start_point,x_area,y_area))
    except Exception as e:
        print(e)


    print("Screenshot taken, parameters of the file are: " + str(screenshots))

    file_path = os.path.join(path, '*')"""




