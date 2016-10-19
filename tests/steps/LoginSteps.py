__author__ = 'MarceloM Guzman'

from resources.uiabstraction.PageObjectFactory import PageObjectFactory


class LoginSteps:
    """
    Steps definition for Login page object.
    """
    _login = None

    def __init__(self):
        self._login = PageObjectFactory.create_login()

    def open_url(self, url):
        """

        :param url:
        :return:
        """
        self._login.open_url("http://" + url)

    def close_browser(self):
        """

        :return:
        """
        self._login.close_browser()

    def set_google_search(self, string_to_search):
        """

        :param string_to_search:
        :return:
        """
        self._login.set_google_search(string_to_search)

    def click_search_button(self):
        """

        :return:
        """
        self._login.click_search_button()

    def click_buildbot_link(self):
        """

        :param result_link:
        :return:
        """
        self._login.click_buildbot_link()

    def click_robot_framework_link(self):
        """

        :return:
        """
        self._login.click_robot_framework_link()

    def verify_if_buildbot_title_is_displayed(self):
        """

        :return:
        """
        self._login.verify_if_buildbot_title_is_displayed()

    def verify_if_fork_me_option_is_displayed(self):
        """

        :return:
        """
        self._login.verify_if_fork_me_option_is_displayed()

    def verify_if_robot_framework_title_is_displayed(self):
        """

        :return:
        """
        self._login.verify_if_robot_framework_title_is_displayed()
