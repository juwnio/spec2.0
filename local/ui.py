import tkinter as tk
from task_processor import process_task

def start_ui():
    root = tk.Tk()
    root.title("Spec")
    
    entry = tk.Entry(root, width=50)
    entry.pack(pady=10)
    
    def submit_task():
        task = entry.get()
        process_task(task)
    
    submit_button = tk.Button(root, text="Submit", command=submit_task)
    submit_button.pack(pady=5)
    
    root.mainloop()
