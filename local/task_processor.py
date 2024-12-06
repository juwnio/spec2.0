import screenshot
import actions
from cloud.task_api import send_to_screen_ai
from cloud.sync import sync_with_cloud

def process_task(task):
    initial_screenshot = screenshot.take_screenshot()
    response = send_to_screen_ai(task, initial_screenshot)
    execute_actions(response)

def execute_actions(response):
    for action in response['actions']:
        if action['type'] == 'click':
            actions.click(action['button'], action['x'], action['y'])
        elif action['type'] == 'type':
            actions.type_text(action['text'])
        screenshot.take_screenshot()
        sync_with_cloud()
