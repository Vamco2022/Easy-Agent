import os
import sys

#BAN_list = {}

def env_command_fileControl(id : str, path : str, fileName : str, controlType : str,lines :str, inf : str):
    file_path = ".\\environments\\" + id + path + "\\" + fileName
    # operation_file_path = ".\\environments\\" + id + path + "\\operation_list.txt"
    # with open(operation_file_path, 'r', encoding='utf-8') as f:
    #     for line in f:
    #         if not line.startswith("#"):
    #             BAN_list[line.split(" ")[0]] = 1

    if not os.path.exists(file_path):
        return [f"{fileName} is not exists!", "Failed"]

    if controlType == 'w':
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(inf)
            return [f"Succeed to write {fileName}!", "Succeed"]
    elif controlType == 'p':
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(inf)
            return [f"Succeed to write {fileName}!", "Succeed"]
    elif controlType == 'r':
        os.rename(file_path, inf)
        return [f"Succeed to rename {fileName} to {inf}!", "Succeed"]
    elif controlType == 'd':
        os.remove(file_path)
        return [f"Succeed to delete {fileName}!", "Succeed"]
    elif controlType == 'c':
        line = lines.split(" - ")
        datas = []
        with open(file_path, 'r', encoding='utf-8') as f:
            last = f.readlines()

        for i in range(len(last)):
            if not ((i + 1) >= int(line[0]) and (i + 1) <= int(line[1])):
                datas.append(last[i])

        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(datas)

        return [f"Succeed to edit {lines} lines!", "Succeed"]

    return [f"{controlType} is not supported!", "Failed"]