from robocorp.tasks import task, task_cache
from robocorp import windows, log
from robocorp.windows import WindowElement
from RPA.Desktop.Windows import Windows
import os, json, time

@task_cache
def get_locators(task) -> dict:
    # Load image locators from locators.json
    with open("locators.json", "r") as file:
        locators = json.load(file)
    yield locators

def open_calculator() -> WindowElement:
    windows.desktop().windows_run("calc.exe")
    window = windows.find_window('regex:.*Calculator')
    return window

def clear_calculator(window: WindowElement):
    """
    Clear previous calculations by just sending a bunch of backspaces as key events
    """
    window.send_keys('{BACK}{BACK}{BACK}{BACK}')

def click_image_by_alias(window: WindowElement, alias: str):
    locators = get_locators(task)
    # Get the path to the image from the locators
    image_path = locators[alias]["path"]
    print(image_path)
    # Find the image on the screen
    #matches = recognition.find_template(image_path, confidence=locators[alias]["confidence"]/100)
    
    #locator = f'coordinates:{matches[0].center.x},{matches[0].center.y}'
    #locator = f'offset:10,10'

    # If a match is found, click on the center of the matched region
    #window.click(locator)
    #time.sleep(2)
    

def calculate_using_image_locators(window: WindowElement):
    """
    Automation using image-based locators is by far the slowest and most brittle way.
    Image-recognitions takes a lot of resources, resolution, color, theme changes, etc. all break the automation
    """
    click_image_by_alias(window, '9')
    click_image_by_alias(window, 'plus')
    click_image_by_alias(window, '5')
    click_image_by_alias(window, 'eq')

def log_results(window: WindowElement, screenshot_file: str):
    result = window.get_value('id:CalculatorResults')
    log.info(result)
    result = os.path.join(os.environ.get('ROBOT_ARTIFACTS'), screenshot_file)
    window.screenshot(result)

@task
def notepad_automation():
    """
    Demostrates different locator patterns to automate Windows applications
    """
    window = open_calculator()
    try:
        window.foreground_window()

        calculate_using_image_locators(window)
        log_results(window, 'result-with-send-keys.png')

    finally:
        window.close_window()


