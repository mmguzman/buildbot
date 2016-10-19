__author__ = 'Silvia Valencia'

from DatabaseLibrary import DatabaseLibrary

from GlobalVariables import DB_API_MODULE_NAME, DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT


class Singleton:
    def __init__(self, klass):
        self.klass = klass
        self._instance = None

    def __call__(self, *args, **kwds):
        if self._instance is None:
            self._instance = self.klass(*args, **kwds)
        return self._instance


@Singleton
class DatabaseManager:
    _instance = None

    def __init__(self):
        self._instance = DatabaseLibrary()
        self._instance.connect_to_database(DB_API_MODULE_NAME, DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT)

    def get_instance(self):
        if self._instance is None:
            self._instance = DatabaseManager()
        return self._instance
