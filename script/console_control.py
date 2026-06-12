import os

#引用自https://geek-docs.com/python/python-ask-answer/216_tk_1704601297.html
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
