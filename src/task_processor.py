import google.generativeai as genai
import os
import time
from PIL import ImageGrab
import numpy as np
import cv2
from image_utils import split_screenshot_into_grids

class TaskProcessor:
    def __init__(self):
        self.api_key = "AIzaSyCduXDOyg80tDJVeZUW0M5s6p2B7Khu30M"  # Make sure to replace with your actual API key
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        self.grid_size = 5  # Define the grid size (5x5 grid for now)

    def capture_screenshot(self):
        screenshot = ImageGrab.grab()  # Capture the entire screen
        screenshot_path = "screenshot.png"
        
        # Save the screenshot using Pillow
        screenshot.save(screenshot_path)

        # Convert to OpenCV format for further processing
        screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        cv2.imwrite(screenshot_path, screenshot_cv)

        print(f"Screenshot saved to {screenshot_path}")
        return screenshot_path

    def process_task(self, task_text, screenshot_path, executor):
        # Split screenshot into grids
        grid_tiles = split_screenshot_into_grids(screenshot_path, self.grid_size)

        # Process each grid tile and send it to Gemini
        for i, grid_tile in enumerate(grid_tiles):
            grid_position = (i // self.grid_size, i % self.grid_size)
            self.process_grid_tile(grid_tile, task_text, grid_position, executor)

    def process_grid_tile(self, grid_tile, task_text, grid_position, executor):
        content = f"Task: {task_text}\nGrid Position: {grid_position}\nAnalyze the content of this section for actionable commands."
        
        grid_tile_path = "grid_tile.png"
        cv2.imwrite(grid_tile_path, grid_tile)

        # Send the grid tile to Gemini API for processing
        response = self.model.generate_content(content)

        print(f"Gemini response for grid {grid_position}: {response.text}")

        commands = self.parse_response(response.text)
        if commands:
            print(f"Commands received for grid {grid_position}: {commands}")
            executor.execute(commands)

        # Clean up by deleting the temporary grid tile image
        os.remove(grid_tile_path)

    def parse_response(self, response_text):
        commands = []
        if '"action": "move"' in response_text:
            coordinates = [500, 300]  # Example coordinates
            commands.append({"action": "move", "coordinates": coordinates})
        elif '"action": "click"' in response_text:
            commands.append({"action": "click", "button": "left"})
        elif '"action": "type"' in response_text:
            commands.append({"action": "type", "text": "Hello World"})
        elif '"action": "complete"' in response_text:
            commands.append({"action": "complete"})
        return commands

    def context(self):
        return """
        # Task Instructions for Gemini AI

        1. **Process one tile at a time**: Wait until all 25 grid tiles are processed before responding with any action. Only one action per grid.
        2. **Only use mouse actions**: Move to coordinates, click (left or right), and type text. No keyboard shortcuts.
        3. **Do not provide descriptive responses**: Provide only actions like move, click, and type in JSON format.
        4. **Coordinates**: Ensure coordinates are relative to the grid.
        5. **Completion**: Only respond with `{"action": "complete"}` when the task is complete.
        """
