import pyautogui
import time
time.sleep(5)
pyautogui.typewrite('2')
while True:
    time.sleep(1)
    pyautogui.typewrite('1')
    time.sleep(1)
    pyautogui.press('backspace')
    time.sleep(1)
    
