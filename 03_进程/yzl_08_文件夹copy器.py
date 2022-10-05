import multiprocessing
import os
import time
import random


def copy_file(file_name, old_name, new_name):
    """完成拷贝任务"""
    print("======>从%s到%s,文件名是%s" % (old_name, new_name, file_name))
    old_f = open(old_name + "/" + file_name, "rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_name + "/" + file_name, "wb")
    new_f.write(content)
    new_f.close()


def main():
    # 1. 获取要拷贝的文件夹的名字
    old_name = input("请输入你要拷贝的文件名:")

    # 2. 创建一个新的文件夹用来拷贝
    try:
        new_name = old_name + "[附件]"
        os.mkdir(new_name)
    except:
        pass

    # 3. 获取所有要拷贝文件夹中的文件名  listdir()
    file_names = os.listdir(old_name)
    print(file_names)

    # 4. 创建进程池  进程池里的任务出现异常会执行，但是不会打印异常信息
    po = multiprocessing.Pool(5)

    # 5. 向进程池里添加拷贝的文件
    for file_name in file_names:
        po.apply_async(copy_file, args=(file_name, old_name, new_name))

    po.close()
    po.join()


if __name__ == "__main__":
    main()