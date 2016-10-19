import os
from platform import system

from robot.libraries.BuiltIn import BuiltIn


try:
    from robot.libraries.BuiltIn import RobotNotRunningError
except ImportError:
    RobotNotRunningError = AttributeError

# ************************** Browser ******************************
try:
    BROWSER = BuiltIn().get_variable_value("${BROWSER}")
except RobotNotRunningError:
    BROWSER = None

try:
    IMPLICIT_WAIT = BuiltIn().get_variable_value("${IMPLICIT_WAIT}")
except RobotNotRunningError:
    IMPLICIT_WAIT = 20

try:
    EXPLICIT_WAIT = BuiltIn().get_variable_value("${EXPLICIT_WAIT}")
except RobotNotRunningError:
    EXPLICIT_WAIT = 20

try:
    TEMPLATE = BuiltIn().get_variable_value("${TEMPLATE}")
except RobotNotRunningError:
    TEMPLATE = None


# ************************** Settings ******************************
if system() == "Windows":
    CHROME_DRIVER_PATH = os.path.join(os.getcwd(), 'drivers', 'chromedriver.exe')
    IE_DRIVER_PATH = os.path.join(os.getcwd(), 'drivers', 'IEDriverServer.exe')
elif system() == "Darwin" or system() == "Linux":
    CHROME_DRIVER_PATH = os.path.join(os.getcwd(), 'drivers', 'chromedriver')

SELENIUM_SERVER_JAR = os.path.join(os.getcwd(), 'drivers', 'selenium-server-standalone.jar')
DOWNLOAD_PATH = os.path.join(os.getcwd(), 'downloads')
