__author__ = 'Silvia Valencia'

from resources.commons.DatabaseManager import DatabaseManager


def get_folder_path_id_from_file_path(folder_path, folder_name):
    """Gets the folder path id of a folder, the folder is identified by the given ``folder_path`` and
    ``folder_name`` arguments.

    Example:
    | ***** Variables *****
    | @{folder path} =  snowserver_wnv  2012 Bare Bones Test Files  Images  Files with XMP
    |
    | ***** Test Cases *****
    | Test Example
    |       ${path_id} =  Get Folder Content   ${folder path}   @{folder path}[2]
    """
    db = DatabaseManager().get_instance()
    path_id = 1
    for folder in folder_path:
        if folder == "osx_wnv": # This is only for OSX server name
            folder = "osx108svr_wnv"
        folder_info = db.query("select FileID, PathID from path where FileID = (select FileID from file where FileName = '" + 
                          folder + "' and PathID = " + str(path_id) + " );")
        path_id = folder_info[0][1]
        if folder == folder_name:
            break
    return path_id


def get_folder_content(folder_path, folder_name):
    """Gets the folder and files that belongs to a folder, the folder is identified by the given ``folder_path`` and
    ``folder_name`` arguments.

    Example:
    | ***** Variables *****
    | @{folder path} =  snowserver_wnv  2012 Bare Bones Test Files  Images  Files with XMP
    |
    | ***** Test Cases *****
    | Test Example
    |       @{folder content} =  Get Folder Content   ${folder path}   @{folder path}[2]
    |       Log To Console  @{folder content}

    Returns a list of tuples. E.g: (('_H1G5482.CR2',), ('Files with XMP',), ('FPO File Formats',),
    ('MA_test2_150905_01_004.TIF',))
    """
    db = DatabaseManager().get_instance()
    path_id = get_folder_path_id_from_file_path(folder_path, folder_name)
    folder_content = db.query("SELECT FileName FROM file WHERE PathID = " + str(path_id) + " and !(FinderFlags & 0x4000);") #16384 = 0x4000 => All but hidden elements
    return folder_content
