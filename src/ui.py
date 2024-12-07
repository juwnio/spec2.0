from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, QLabel
import time

class TaskInterface(QWidget):
    def __init__(self, task_processor, executor, screenshot_handler, logger):
        super().__init__()
        self.task_processor = task_processor
        self.executor = executor
        self.screenshot_handler = screenshot_handler
        self.logger = logger
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Spec Task Interface")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.task_input = QLineEdit(self, placeholderText="Enter a task...")
        self.submit_button = QPushButton("Submit Task", self)
        self.cancel_button = QPushButton("Cancel Task", self)
        self.output_log = QTextEdit(self)
        self.output_log.setReadOnly(True)
        self.loading_label = QLabel("")

        layout.addWidget(self.task_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.cancel_button)
        layout.addWidget(self.output_log)
        layout.addWidget(self.loading_label)

        self.setLayout(layout)
        self.submit_button.clicked.connect(self.handle_task_submission)
        self.cancel_button.clicked.connect(self.handle_task_cancelation)

    def handle_task_submission(self):
        task_text = self.task_input.text()
        if task_text.strip():
            self.loading_label.setText("Processing...")
            screenshot = self.screenshot_handler.capture()
            self.task_processor.process_task(task_text, screenshot, self.executor)
            self.loading_label.setText("Task Completed")
        else:
            self.logger.log("No task entered.")

    def handle_task_cancelation(self):
        self.executor.cancel_current_task()
        self.logger.log("Task canceled.")
        self.loading_label.setText("Task Canceled")
