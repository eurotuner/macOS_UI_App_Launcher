#!/usr/local/bin/python3

import pyautogui
import time

#TODO: Add interaction features with first party apps
#TODO: Add error feature 

def pyfind(self):
    pyautogui.hotkey('command', 'space')
    pyautogui.typewrite(self, interval=0.8);time.sleep(2);pyautogui.hotkey('return')

def app_launch():
   pyfind('App Store')
   pyfind('Calculator')
   pyfind('Calendar')
   pyfind('Chess')
   pyfind('Contacts');time.sleep(3)
   pyfind('Dictionary')
   pyfind('FaceTime')
   pyfind('iBook')
   pyfind('iTunes')
   pyfind('Keynote')
   pyfind('Mail')
   pyfind('Maps')
   pyfind('Messages');time.sleep(3)
   pyfind('Mission Control')
   pyfind('Notes')
   pyfind('Numbers')
   pyfind('Pages')
   pyfind('Photo Booth')
   pyfind('Photos')
   pyfind('Preview')
   pyfind('Reminders')
   pyfind('Safari')
   pyfind('Siri')
   pyfind('Stickies')
   pyfind('System Preferences')
   pyfind('Time Machine')

app_launch()
