import pyautogui
import time

class TaskExecutor:
    def __init__(self, logger):
        self.logger = logger
        self.cancel_flag = False

    def execute(self, commands):
        for command in commands:
            if self.cancel_flag:
                self.logger.log("Task execution canceled.")
                break

            action = command.get("action")
            if action == "move":
                x, y = command.get("coordinates", [0, 0])
                self.logger.log(f"Moving cursor to ({x}, {y})")
                pyautogui.moveTo(x, y, duration=0.5)  # Improved movement speed
            elif action == "click":
                button = command.get("button", "left")
                self.logger.log(f"Clicking {button} button")
                pyautogui.click(button=button)
            elif action == "type":
                text = command.get("text", "")
                self.logger.log(f"Typing text: {text}")
                pyautogui.typewrite(text, interval=0.05)
            else:
                self.logger.log(f"Unknown action: {action}")

            time.sleep(3)  # Add a 3-second delay between actions

    def cancel_current_task(self):
        self.cancel_flag = True
        self.logger.log("Task execution canceled.")
