__author__ = 'MarceloM Guzman'

from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from resources.commons.DriverManager import DriverManager


class LoginPageBase(object):
    """
    Page object modeling the structure and operations of the Portal LoginPageBase page.
    """
    _driver = None
    _wait = None

    # Selectors
    search_text_box = (By.ID, "lst-ib")
    search_button = (By.NAME, "btnG")
    navigation_content = (By.ID, "navcnt")
    buildbot_link = (By.LINK_TEXT, "Buildbot")
    robot_framework_link = (By.LINK_TEXT, "Robot Framework")
    fork_me_ribbon_content = (By.XPATH, "//a[@class='ribbon red']/span[text()='Fork me on GitHub!']")

    def __init__(self):
        self._driver = DriverManager().get_instance().get_driver()
        self._wait = DriverManager().get_instance().get_wait()
        #self.theme = theme

    def open_url(self, url):
        """
        Opens the browser with Xinet Portal.
        :param url: URL of the Xinet server.
        """
        self._driver.get(url)

    def close_browser(self):
        """

        :return:
        """
        self._driver.quit()

    def set_google_search(self, string_to_search):
        """

        :param string_to_search:
        :return:
        """
        self._driver.find_element(*self.search_text_box).clear()
        self._driver.find_element(*self.search_text_box).send_keys(string_to_search)

    def click_search_button(self):
        """

        :return:
        """
        self._driver.find_element(*self.search_button).click()
        self._wait.until(ec.visibility_of_element_located(self.navigation_content))

    def click_buildbot_link(self):
        """

        :return:
        """
        buildbot_page_title = "Buildbot"
        self._driver.find_element(*self.buildbot_link).click()
        self._wait.until(ec.title_is(buildbot_page_title), "The page title is not: " + buildbot_page_title)

    def click_robot_framework_link(self):
        """

        :return:
        """
        rf_page_title = "Robot Framework"
        self._driver.find_element(*self.robot_framework_link).click()
        self._wait.until(ec.title_is(rf_page_title), "The page title is not: " + rf_page_title)

    def verify_if_buildbot_title_is_displayed(self):
        """

        :return:
        """
        BuiltIn().should_be_equal(self._driver.title, "Buildbot")

    def verify_if_fork_me_option_is_displayed(self):
        """

        :return:
        """
        is_fork_me_option_displayed = self._driver.find_element(*self.fork_me_ribbon_content).is_displayed()
        BuiltIn().should_be_true(is_fork_me_option_displayed, msg="The Fork Me On GitHub! message is not displayed.")


    def verify_if_robot_framework_title_is_displayed(self):
        """

        :return:
        """
        title = self._driver.title
        BuiltIn().should_be_equal(title, "Robot Framework")
