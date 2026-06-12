import os
import sys

def env_command_createFile(id : str, path : str, type : str,fileName : str):
    file_path = ".\\environments\\" + id + path + "\\" + fileName
    if os.path.exists(file_path):
        return [f"{fileName} already exists!", "Failed"]
    if type == "folder":
        os.makedirs(file_path)
        return [f"Succeed to create the folder {fileName}!", "Succeed"]
    elif type == "file":
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("")
        return [f"Succeed to create the file {fileName}!", "Succeed"]
    return [f"{type} is not supported!", "Failed"]
