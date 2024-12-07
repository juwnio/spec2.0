import pyautogui
import time

class TaskExecutor:
    def __init__(self):
        pass  # No logger needed

    def execute(self, commands):
        for command in commands:
            if command["action"] == "move":
                self.move_cursor(command["coordinates"])
            elif command["action"] == "click":
                self.click(command["button"])
            elif command["action"] == "type":
                self.type_text(command["text"])
            elif command["action"] == "complete":
                print("Task complete. Ending execution.")
                break
            else:
                print(f"Unknown action: {command['action']}")

    def move_cursor(self, coordinates):
        x, y = coordinates
        print(f"Moving cursor to {x}, {y}")
        pyautogui.moveTo(x, y, duration=0.5)
        time.sleep(0.5)

    def click(self, button):
        print(f"Clicking {button} button")
        pyautogui.click(button=button)
        time.sleep(0.5)

    def type_text(self, text):
        print(f"Typing text: {text}")
        pyautogui.typewrite(text, interval=0.1)
        time.sleep(1)
