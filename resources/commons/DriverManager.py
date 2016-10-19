__author__ = 'Silvia Valencia'

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from resources.libraries.Utils import update_ie_download_directory_registry, set_ie_to_avoid_download_popup_registry
from GlobalVariables import *


class Singleton:
    def __init__(self, klass):
        self.klass = klass
        self._instance = None

    def __call__(self, *args, **kwds):
        if self._instance is None:
            self._instance = self.klass(*args, **kwds)
        return self._instance

@Singleton
class DriverManager:
    _driver = None
    _wait = None
    _instance = None

    def __init__(self):
        self.initialize_webdriver()

    def set_firefox_profile(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.folderList', 2)
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference("browser.download.manager.showAlertOnComplete", False)
        profile.set_preference('browser.download.dir', DOWNLOAD_PATH)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                               "application/msword, application/csv, application/ris, text/csv, image/png, "
                               "application/pdf, text/html, text/plain, application/zip, application/x-zip, "
                               "application/x-zip-compressed, application/download, application/octet-stream")
        return profile

    def initialize_webdriver(self):
        try:
            if self._driver is None and BROWSER is not None:
                if BROWSER.lower() == "firefox":
                    self._driver = webdriver.Firefox(self.set_firefox_profile())
                elif BROWSER.lower() == "chrome":
                    chrome_options = webdriver.ChromeOptions()
                    preferences = {"download.default_directory": DOWNLOAD_PATH}
                    chrome_options.add_experimental_option("prefs", preferences)
                    self._driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, chrome_options=chrome_options)
                elif BROWSER.lower() == "safari":
                    self._driver = webdriver.Safari(SELENIUM_SERVER_JAR)
                elif BROWSER.lower() == "ie":
                    update_ie_download_directory_registry()
                    set_ie_to_avoid_download_popup_registry()
                    caps = DesiredCapabilities.INTERNETEXPLORER
                    caps['ignoreProtectedModeSettings'] = True
                    self._driver = webdriver.Ie(IE_DRIVER_PATH, capabilities=caps)
                self._driver.implicitly_wait(float(IMPLICIT_WAIT))
                self._driver.maximize_window()
                self._wait = WebDriverWait(self._driver, float(EXPLICIT_WAIT))
        except TypeError as e:
            print e.message

    def get_instance(self):
        if self._instance is None or self._driver is None:
            self._instance = DriverManager()
        return self._instance

    def get_driver(self):
        return self._driver

    def get_wait(self):
        return self._wait
