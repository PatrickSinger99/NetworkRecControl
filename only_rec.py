import pyautogui
import time

h, m = 2, 20

pyautogui.hotkey('alt', 'x', interval=.2)
print("Pressed ALT-X")
t_sec = (h * 60 + m) * 60
print(f"Waiting for {h}hr {m}min ({t_sec}sec)")
time.sleep(t_sec)
pyautogui.hotkey('alt', 'y', interval=.2)
print("Pressed ALT-y")
