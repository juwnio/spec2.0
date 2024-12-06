import pyautogui
import time

def take_screenshot():
    time.sleep(2)  # Delay for loading
    screenshot = pyautogui.screenshot()
    screenshot_path = "current_screen.png"
    screenshot.save(screenshot_path)
    return screenshot_path
