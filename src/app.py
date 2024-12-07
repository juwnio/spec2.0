import time
from task_processor import TaskProcessor
from executor import TaskExecutor
from tkinter import Tk, Label, Button, Entry

# Add retry mechanism for API calls (in case of quota issues)
def retry_api_call(func, retries=3, delay=5):
    attempt = 0
    while attempt < retries:
        try:
            return func()
        except Exception as e:
            print(f"Error: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
            attempt += 1
    print("API quota exceeded or error occurred.")
    return None

# Tkinter UI class
class TaskInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Interface")

        # Task input
        self.label = Label(self.master, text="Enter your task:")
        self.label.pack()

        self.task_entry = Entry(self.master)
        self.task_entry.pack()

        # Submit button
        self.submit_button = Button(self.master, text="Submit", command=self.submit_task)
        self.submit_button.pack()

    def submit_task(self):
        # Retrieve the task entered by the user
        task_text = self.task_entry.get()

        # Initialize TaskProcessor and TaskExecutor
        task_processor = TaskProcessor()
        task_executor = TaskExecutor()

        # Capture screenshot and process the task
        screenshot_path = task_processor.capture_screenshot()

        # Retry logic for API call in case of quota exhaustion
        response = retry_api_call(lambda: task_processor.process_task(task_text, screenshot_path, task_executor))

        if response is not None:
            print("Task successfully processed!")
        else:
            print("Task failed due to API issues.")

# Main function to run the Tkinter interface
def main():
    # Initialize Tkinter window
    root = Tk()
    interface = TaskInterface(root)

    # Start the Tkinter main loop to show the interface
    root.mainloop()

if __name__ == "__main__":
    main()
