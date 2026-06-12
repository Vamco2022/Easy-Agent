import os
import sys

def env_command_readFile(id : str, path : str):
    try:
        file_path = ".\\environments\\" + id + path
        data = ""
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read()
    except PermissionError:
        return ["Failed, please check that is it a file(probably not a readable file or folder)", f"Failed path:{path}"]
    except FileNotFoundError:
        return ["Failed, file is not exist", f"Failed path:{path}"]

    return [data, f"Succeed, path:{path}"]