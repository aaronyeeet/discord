import pyautogui
import time
# wait 5 seconds
time.sleep(5)
# type 2
pyautogui.typewrite('2')
# loop start
while True:
    # wait 1 second
    time.sleep(1)
    # type 1
    pyautogui.typewrite('1')
    # wait 1 second
    time.sleep(1)
    # press backspace
    pyautogui.press('backspace')
    # wait 1 second
    time.sleep(1)
    
    
