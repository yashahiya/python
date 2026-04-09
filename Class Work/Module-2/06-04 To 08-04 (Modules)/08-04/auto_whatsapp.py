import pywhatkit
import pyautogui
import time

number="+917228833203"

pywhatkit.sendwhatmsg_instantly(number,"start")
time.sleep(5)

messages=["msg 1","masg 2","msg 3"]

for msg in messages:
    pyautogui.write(msg)
    pyautogui.press("enter")
    time.sleep(5)