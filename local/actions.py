import pyautogui

def click(button, x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click(button=button)

def type_text(text):
    pyautogui.typewrite(text)
