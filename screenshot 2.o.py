import pyautogui
import datetime
import os

def take_fullscreen_screenshot():
    # Create a directory to save the screenshot
    save_dir = "screenshots"
    os.makedirs(save_dir, exist_ok=True)

    # Generate a filename with the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot_{timestamp}.png"
    filepath = os.path.join(save_dir, filename)

    # Take a screenshot of the full screen
    screenshot = pyautogui.screenshot()

    # Save the screenshot
    screenshot.save(filepath)
    print(f"✅ Screenshot saved: {filepath}")

# Run it
take_fullscreen_screenshot()
