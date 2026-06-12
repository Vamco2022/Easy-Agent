import time

def get_time():
    #按YYYY-MM-DD HH:MM:SS格式获取当前时间
    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return [times, times]