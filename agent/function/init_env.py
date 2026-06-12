import os
import random
import sys

from script.randomID_generate import generate_random_id

def init_env():
    folder_path = ".\\environments\\"
    folder_name = generate_random_id()
    os.makedirs(folder_path + folder_name)
    return [f"Succeed to create the env! The ID is {folder_name}","Succeed"]