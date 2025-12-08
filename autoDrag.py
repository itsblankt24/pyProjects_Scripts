import sys
import pyautogui 
import os

def dragged(amount):
    total = amount
    current = 1
    os.system('cls') 
    print("Starting now...")
    while amount > 0:
        pyautogui.drag(0, -30, .3, button='left')
        pyautogui.move(0,30)
        print(f"Dragged {current}/{total} times.") 
        current +=1 
        amount -=1

try:
    amount = int(input("How many times do you want to drag? "))
except ValueError:
    print("Please enter a valid number next time.")
    sys.exit()
print("Move your mouse to where you would like to start from")
start = input("Let me know when you are ready to start.\n Type [y] or [n].\n")
if start == 'y':
    dragged(amount)
    os.system('cls')    
    print("Task completed successfully.")   
else:
    print("Exiting program. Try again when ready.")
    sys.exit()
