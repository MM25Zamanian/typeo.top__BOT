from klembord import init, get_text
from pyautogui import press
from time import sleep

init()

sleep(15)
c = str(get_text())
print(c)
for i in c:
    press(i)
    sleep(0.005)
