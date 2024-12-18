import pyautogui
import time

pyautogui.PAUSE = 0.3

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=966, y=620)
time.sleep(2)
pyautogui.write("www.google.com")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("Testing pyautogui")