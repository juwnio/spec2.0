from PIL import ImageGrab
import time

class ScreenshotHandler:
    def __init__(self, logger):
        self.logger = logger

    def capture(self):
        # Capture the screenshot
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_path = f"screenshot_{timestamp}.png"
        image = ImageGrab.grab()
        image.save(screenshot_path)
        self.logger.log(f"Screenshot saved to {screenshot_path}")
        
        # Return the path to the screenshot for use in sending
        return screenshot_path
