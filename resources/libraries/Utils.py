__author__ = 'MarceloM Guzman'

import os
import time
import zipfile
from platform import system

from resources.commons.GlobalVariables import DOWNLOAD_PATH


def get_directory_number_of_files(directory_path):
    """
    Returns the number of files within a directory.
    :param directory_path: The path to check the number of files.
    :return: The number of files present in a directory.
    """
    return len(os.listdir(directory_path))


def wait_until_file_is_created(file_path):
    """
    Waits until the file is created or present.
    :param file_path: The path where the file is created.
    """
    count = 0
    while count < 10 and os.path.exists(file_path) == True:
        time.sleep(1)
        count += 1


def wait_until_file_is_downloaded(file_path):
    """
    Waits until the file is downloaded.
    :param file_path: The path where the file will be downloaded.
    """
    while True:
        if os.path.isfile(file_path + ".part"):
            time.sleep(10)
        elif os.path.isfile(file_path):
            break
        else:
            time.sleep(10)


def is_file_present_in_directory(file_path):
    """
    Verifies if a file is present.
    :param file_path: The path to verify the presence of the file.
    :return: True if the file is present, otherwise False.
    """
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return True
    else:
        return False


def extract_file(file_path, path_to_extract=DOWNLOAD_PATH):
    """
    Extract all the files from a compressed file.
    :param file_path: The path of the file to extract.
    :param path_to_extract: The path where to extract fhe file.
    """
    z = zipfile.ZipFile(file_path)
    z.extractall(path_to_extract)


def update_ie_download_directory_registry():
    """
    Updates the Windows Registry key to change the default IE download directory.
    """
    if system() == "Windows":
        import _winreg
        key_val = r'Software\Microsoft\Internet Explorer\Main'
        try:
            key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, key_val, 0, _winreg.KEY_ALL_ACCESS)
        except Exception as e:
            print e
            key = _winreg.CreateKey(_winreg.HKEY_CURRENT_USER, key_val)
        _winreg.SetValueEx(key, "Default Download Directory", 0, _winreg.REG_SZ, DOWNLOAD_PATH)
        _winreg.CloseKey(key)


def set_ie_to_avoid_download_popup_registry():
    """
    Updates the Windows Registry to add a new key and binary value to avoid download popup.
    """
    if system() == "Windows":
        import _winreg
        key_val = r'Software\Microsoft\Windows\Shell\AttachmentExecute\{0002DF01-0000-0000-C000-000000000046}'
        try:
            key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, key_val, 0, _winreg.KEY_ALL_ACCESS)
        except Exception as e:
            print e
            key = _winreg.CreateKey(_winreg.HKEY_CURRENT_USER, key_val)
        _winreg.SetValueEx(key, "WinRAR.ZIP", 0, _winreg.REG_BINARY, "")
        _winreg.SetValueEx(key, "CompressedFolder", 0, _winreg.REG_BINARY, "")
        _winreg.CloseKey(key)
