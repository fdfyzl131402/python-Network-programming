import multiprocessing
import time

g_list = []


# 添加数据的任务
def add_list():
    for i in range(3):
        g_list.append(i)
        print("add:", i)
        time.sleep(0.2)
    print("添加完成：", g_list)


# 读取数据的任务
def read_list():
    print("add:", g_list)


# 注意： 对于linux和mac，主进程执行的代码不会在子进程中进行拷贝，但是对于windows来说，子进程会拷贝
# 对于window来说，也就相当于递归没有出口，出现死循环，无限创建子进程
# 解决办法就是判断是否是主模块
def main():
    # 添加数据给子进程
    add_process = multiprocessing.Process(target=add_list)
    # 读取数据给子进程
    read_process = multiprocessing.Process(target=read_list)
    add_process.start()
    # 当前进程（主进程）等待添加数据执行完之后再去执行后续代码
    add_process.join()
    read_process.start()


if __name__ == "__main__":
    main()


