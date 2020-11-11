import pyautogui

pyautogui.hotkey('Win')
pyautogui.typewrite('Telegram')
pyautogui.PAUSE = 2
pyautogui.keyDown('Enter')
pyautogui.PAUSE = 0.001
for a in range(100000):
    pyautogui.write("Text", interval=0.001)
    pyautogui.keyDown('Enter')
