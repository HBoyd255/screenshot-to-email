from PIL import ImageGrab

# Capture the entire screen
screenshot = ImageGrab.grab()

# Save the screenshot to a file
screenshot.save("screenshot.png")

# Close the screenshot
screenshot.close()

from todoist_api_python.api import TodoistAPI
from modules.file_utils import text_file_to_string, save_object, load_object

API_TEXT_FILE = "secrets/api_key.txt"
API_KEY = text_file_to_string(API_TEXT_FILE)
api = TodoistAPI(API_KEY)

try:
    task = api.add_task(content="Buy Milk", project_id="2203306141")
    print(task)
except Exception as error:
    print(error)
