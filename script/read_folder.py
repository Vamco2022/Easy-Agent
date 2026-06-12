import os

def list_dir(folder):
    yaml = [os.path.join(folder, file) for file in os.listdir(folder)]
    return yaml