import multiprocessing
import os


def copy_file(q, file_name, old_name, new_name):
    """完成拷贝任务"""
    # print("======>从%s到%s,文件名是%s" % (old_name, new_name, file_name))
    old_f = open(old_name + "/" + file_name, "rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_name + "/" + file_name, "wb")
    new_f.write(content)
    new_f.close()

    q.put(file_name)


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

    # 5.添加一个队列
    q = multiprocessing.Manager().Queue()

    # 6. 向进程池里添加拷贝的文件
    for file_name in file_names:
        po.apply_async(copy_file, args=(q, file_name, old_name, new_name))

    po.close()
    # po.join()
    all_file_names = len(file_names)
    copy_date = 0
    while True:
        file_name = q.get()
        # print("已经完成的copy:%s" % file_name)
        copy_date += 1
        print("\r已完成的进度：%.2f %%" % (copy_date * 100 / all_file_names), end="")
        if copy_date >= all_file_names:
            break

    print()


if __name__ == "__main__":
    main()