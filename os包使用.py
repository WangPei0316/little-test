"""
这个函数接受文件夹的名称作为输入参数，
返回该文件夹中文件的路径，
以及其包含文件夹中文件的路径。

"""

import os


def print_dir_contents(sPath):
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_dir_contents(sChildPath)
        else:
            print(sChildPath)


sPath = input('路径:')
print_dir_contents(sPath)
