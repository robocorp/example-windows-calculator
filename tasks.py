from robocorp.tasks import task
from robocorp import windows, log
from robocorp.windows import WindowElement
import os, time

def open_calculator() -> WindowElement:
    windows.desktop().windows_run("calc.exe")
    window = windows.find_window('regex:.*Calculator')
    return window

def clear_calculator(window: WindowElement):
    """
    Clear previous calculations by just sending a bunch of backspaces as key events
    """
    window.send_keys('{BACK}{BACK}{BACK}{BACK}')

def add_two_numbers_using_ids(window: WindowElement, first: str, second: str ):
    """
    Automation using locators based on automation id -field values is a solid way
    ...if the target app provides static automation ids
    """
    window.click('id:clearEntryButton')
    window.click(f'id:num{first}Button')
    window.click('id:plusButton')
    window.click(f'id:num{second}Button')
    window.click('id:equalButton')

def add_two_numbers_using_ids(window: WindowElement, first: str, second: str ):
    """
    Automation using locators based on automation id -field values is a solid way
    ...if the target app provides static automation ids
    """
    window.click('id:clearEntryButton')
    window.click(f'id:num{first}Button')
    window.click('id:plusButton')
    window.click(f'id:num{second}Button')
    window.click('id:equalButton')

def add_two_numbers_using_send_keys(window: WindowElement, first: str, second: str ):
    """
    Automation using send_keys() and hotkeys provided by the application is solid and by far the fastest option
    ...if the target app provides keyboard shortcuts
    """
    window.send_keys(f'{first}+{second}=')

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

        add_two_numbers_using_send_keys(window, 9, 5)
        log_results(window, 'result-with-send-keys.png')

        clear_calculator(window)
        add_two_numbers_using_ids(window, 9, 5)
        log_results(window, 'result-with-ids.png')

        clear_calculator(window)
        add_two_numbers_using_ids(window, 9, 5)
        log_results(window, 'result-with-ids.png')
        
        # Check out the logs and compare the durations between:
        # 'add_two_numbers_using_ids' and 'add_two_numbers_using_send_keys'


    finally:
        window.close_window()


