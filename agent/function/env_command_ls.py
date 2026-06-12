import os
import sys

def env_command_ls(id : str, path : str):
    folder_path = ".\\environments\\" + id + path
    #print(folder_path)
    return [str(os.listdir(folder_path)), f"Succeed,path {path}"]

