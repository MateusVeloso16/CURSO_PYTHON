import pyautogui
import time

pyautogui.PAUSE=0.3

print(pyautogui.position())
print(pyautogui.size())

time.sleep(5)
#pyautogui.click(x=578, y=937)
#pyautogui.moveTo(x=538, y=218, duration=3)
#pyautogui.click(x=904, y=341)

pyautogui.write("Se inscreve no canal")
pyautogui.hotkey()
pyautogui.press()

