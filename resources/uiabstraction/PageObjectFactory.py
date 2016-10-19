__author__ = 'MarceloM Guzman'

from resources.uiabstraction.pages.login.LoginPageBase import LoginPageBase


class PageObjectFactory(object):
    """
    Class responsible to design a page implementation according template.
    """

    @classmethod
    def create_login(cls):
        return LoginPageBase()
