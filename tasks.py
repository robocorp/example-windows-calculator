from robocorp.tasks import task
from robocorp import windows, log
from robocorp.windows import WindowElement
from RPA.Desktop import Desktop
import os

def open_calculator() -> WindowElement:
    windows.desktop().windows_run("calc.exe")
    window = windows.find_window('regex:.*Calculator')
    return window

def clear_calculator(window: WindowElement):
    """
    Clear previous calculations by just sending a bunch of backspaces as key events
    """
    window.send_keys('{BACK}{BACK}{BACK}{BACK}')

def calculate_using_send_keys(window: WindowElement, first: str, second: str ):
    """
    Automation using send_keys() and hotkeys provided by the application is solid and by far the fastest option
    ...if the target app provides keyboard shortcuts
    """
    window.send_keys(f'{first}+{second}=')

def calculate_using_ids(window: WindowElement, first: str, second: str ):
    """
    Automation using locators based on automation id -field values is a solid way
    ...if the target app provides static automation ids
    """
    window.click('id:clearEntryButton')
    window.click(f'id:num{first}Button')
    window.click('id:plusButton')
    window.click(f'id:num{second}Button')
    window.click('id:equalButton')

def calculate_using_image_locators(first: str, second: str):
    """
    Automation using image-based locators is the slowest and most brittle form, but sometimes still needed.
    Image recognition takes time and resources
    Changes to resolution, themes and UI changes all can break the automation.

    """
    try:
        desktop = Desktop()
        desktop.click(f'alias:{first}')
        desktop.click('alias:plus')
        desktop.click(f'alias:{second}')
        desktop.click('alias:eq')
    except Exception as e:
        log.critical('Image-based locator not found')
        raise e

def log_results(window: WindowElement, screenshot_file: str):
    result = window.get_value('id:CalculatorResults or name:Result')
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

        calculate_using_send_keys(window, 9, 5)
        log_results(window, 'result-with-send-keys.png')

        clear_calculator(window)
        calculate_using_ids(window, 9, 5)
        log_results(window, 'result-with-ids.png')

        clear_calculator(window)
        calculate_using_image_locators(9, 5)
        log_results(window, 'result-with-images.png')
        
        # Check out the logs for following points:
        # - Compare the durations between: 'calculate_using_ids' and 'calculate_using_send_keys'
        # - Image-based automation will most likely fail:
        #   The image locators are done for the old style of windows calculator.

    finally:
        window.close_window()


