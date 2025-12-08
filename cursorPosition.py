import pyautogui
import time
import sys
import os

while True:
    x, y = pyautogui.position()
    os.system('cls')
    print(f"Mouse Position: X={x}, Y={y}")
    time.sleep(.25)