__author__ = 'MarceloM Guzman'

import os
import random
import string

from robot import utils
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.Screenshot import Screenshot
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    NoSuchWindowException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

from resources.commons.DriverManager import DriverManager
from resources.commons.GlobalVariables import BROWSER


def ready_state_complete(driver):
    """
    Returns true when the document status is complete, otherwise false.
    """
    return driver.execute_script("return document.readyState") == "complete"


def wait_for_load_page():
    """
    Waits until the document status is complete or timeout after explicit wait time.
    """
    wait = DriverManager().get_instance().get_wait()
    wait.until(ready_state_complete, "The page did not finish to load completely.")


def is_element_present(driver, by, value):
    """
    Verifies if an element is present.
    """
    try:
        driver.find_element(by=by, value=value)
    except NoSuchElementException:
        return False
    return True


def found_window(window_name):
    """
    Switch to a new window displayed.
    """

    def predicate(driver):
        try:
            driver.switch_to_window(window_name)
        except NoSuchWindowException:
            return False
        else:
            return True
    return predicate


def select_checkbox(driver, by, value):
    """
    Checks a checkbox element.
    """
    wait = DriverManager().get_instance().get_wait()
    control = (by, value)
    wait.until(ec.visibility_of_element_located(control), "The " + value + " element is not present.")
    checkbox = driver.find_element(by=by, value=value)
    if not checkbox.is_selected():
        checkbox.click()
    else:
        "The element is already checked."


def unselect_checkbox(driver, by, value):
    """
    Unchecks a checkbox element.
    """
    checkbox = driver.find_element(by=by, value=value)
    if checkbox.is_selected():
        checkbox.click()
    else:
        "The  element is already unchecked."


def get_quantity_of_elements_displayed_on_page(driver, by, value):
    """
    Gets the quantity of elements displayed.
    """
    return len(driver.find_elements(by=by, value=value))


@property
def _log_dir():
    variables = BuiltIn().get_variables()
    outdir = variables['${OUTPUTDIR}']
    log = variables['${LOGFILE}']
    log = os.path.dirname(log) if log != 'NONE' else '.'
    return _norm_path(os.path.join(outdir, log))


def _norm_path(path):
    if not path:
        return path
    return os.path.normpath(path.replace('/', os.sep))


def get_screenshot(file_name):
    """
    Takes an screenshot using Selenium Library for Python.
    TEST!
    """
    driver = DriverManager().get_instance().get_driver()
    driver.save_screenshot(file_name)
    image_path = os.getcwd().split(os.sep)[-1] + '/' + file_name
    _embed_screenshot(image_path, "800px")


def _embed_screenshot(path, width):
    """
    Embeds the screenshot to Robot Framework report.
    """
    link = utils.get_link_path(path, _log_dir)
    logger.info('<a href="%s"><img src="%s" width="%s"></a>' % (link, link, width), html=True)


def move_mouse_to_using_actions(driver, by, value):
    """
    Moves the mouse cursor to a location using ActionChains.
    """
    element = driver.find_element(by=by, value=value)
    actions = ActionChains(driver)
    actions.move_to_element(element).click()

    ActionChains(driver).move_to_element(element).perform()


def move_mouse_to(driver, element):
    """
    Moves the mouse cursor to a location using JS.
    """
    javaScript = "var evObj = document.createEvent('MouseEvents');evObj.initMouseEvent(\"mouseover\",true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);arguments[0].dispatchEvent(evObj);"
    driver.execute_script(javaScript, element)


def accept_alert_before_displayed(driver):
    """
    Immediately return True (Accept the alert before displaying it) using JS. 
    """
    driver.execute_script("confirm = function(message){return true;};")
    driver.execute_script("alert = function(message){return true;};")
    driver.execute_script("prompt = function(message){return true;}")


def click_element_stale(driver, by, value):
    """
    Clicks an element retrying if StaleElement exception is displayed.
    """
    count = 0
    found = False
    while count < 3 and not found:
        try:
            element = driver.find_element(by=by, value=value)
            if BROWSER.lower() == "ie":
                click_element(driver, element)
            else:
                element.click()
            found = True
            break
        except StaleElementReferenceException as stale:
            print "Problem type:StaleElementReferenceException \nArgs: by=" + by + " value=" + value + "\n" + str(stale)
        count += 1


def click_element(driver, element):
    """
    Clicks an element using JS.
    """
    driver.execute_script("arguments[0].click();", element)


def scroll_click_element(driver, element):
    """
    Scroll and clicks an element using JS.
    """
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    click_element(driver, element)


def scroll_down():
    """
    Scrolls down the page using JS.
    """
    driver = DriverManager().get_instance().get_driver()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def scroll_down_until_page_loaded():
    """
    Scrolls down until the page finishes loading.
    """
    while True:
        scroll_down()
        if not wait_for_load_page():
            break


def wait_for_option_selected_in_combo(driver, expected_result, by, value):
    """
    Waits for option selected in combo.
    """
    are_equals = False
    type_of_exception = None
    count = 0
    while not are_equals and count < 3:
        try:
            select = Select(driver.find_element(by=by, value=value))
            actual_result = select.first_selected_option.text
            if expected_result == actual_result:
                are_equals = True
        except StaleElementReferenceException as stale:
            print "Problem type:StaleElementReferenceException \nArgs: by=" + by + " value=" + value + "\n" + str(stale)
            type_of_exception = STALE_ELEMENT_REFERENCE_EXCEPTION
        except NoSuchElementException as noSuch:
            print "Problem type:NoSuchElementException \nArgs: by=" + by + " value=" + value + "\n" + str(noSuch)
            type_of_exception = NO_SUCH_ELEMENT_EXCEPTION
        except TimeoutException as timeout:
            print "Problem type:NoSuchElementException \nArgs: by=" + by + " value=" + value + "\n" + str(timeout)
            type_of_exception = TIMEOUT_EXCEPTION
        except Exception as e:
            print "Problem type:Exception \nArgs: by=" + by + " value=" + value + "\n" + str(e)
            type_of_exception = EXCEPTION
        count += 1
    if not are_equals:
        raise_exception(type_of_exception)
    return are_equals


def raise_exception(type_of_exception):
    """
    Raises an exception according to type of exception.
    """
    if type_of_exception == STALE_ELEMENT_REFERENCE_EXCEPTION:
        raise StaleElementReferenceException()
    elif type_of_exception == NO_SUCH_ELEMENT_EXCEPTION:
        raise NoSuchElementException()
    elif type_of_exception == TIMEOUT_EXCEPTION:
        raise TimeoutException()
    elif type_of_exception == EXCEPTION:
        raise Exception()


def accept_and_close_alert(driver):
    """
    Accepts and closes the alert displayed.
    :param driver: Driver instance.
    """
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except NoAlertPresentException:
        print "There is no alert to switch on."


def get_random_name(length=10):
    """
    Gets a random name of 10 length.
    """
    key_list = [random.choice(string.lowercase + string.digits) for _ in range(length)]
    return "".join(key_list)


def accept_alert_and_leave_page(driver):
    """
    Immediately return True to leave actual page using JS.
    """
    driver.execute_script("window.onbeforeunload = function() { if(formIsModified(document.form[0])) { if (confirm('Are you sure you want to leave this page?')) return true; else return false; } }")
    driver.refresh()


def take_screenshot_and_publish_link(test_case_name):
    """
    Take screenshot and publish the image link to the Log file.
    :param test_case_name: The test case name.
    """
    screenshot_directory = "report/screenshots"
    screenshot = Screenshot()
    if not os.path.exists(screenshot_directory):
        os.makedirs(screenshot_directory)
    screenshot.set_screenshot_directory(screenshot_directory)
    path = screenshot._save_screenshot(test_case_name)
    builder_name = path.split(os.sep)[-7]
    image_name = os.path.basename(path)
    print "http://131.106.11.41/buildbot/" + builder_name + "/screenshots/" + image_name
