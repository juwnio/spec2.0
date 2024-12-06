import requests

def send_to_screen_ai(task, screenshot_path):
    url = "https://api.screenai.com/process"
    data = {'task': task, 'screenshot': open(screenshot_path, 'rb')}
    response = requests.post(url, files=data)
    return response.json()
