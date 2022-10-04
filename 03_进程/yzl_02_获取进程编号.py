import multiprocessing
import os
import time


def test1():
    # 获取当前进程的编号, 并获取当前进程对象，知道该编号是那个进程的
    text1_process = os.getpid()
    print(f"当前进程的编号: {text1_process}，{multiprocessing.current_process()}")
    # 获取当前的进程的父进程编号
    text1_process_parent_id = os.getppid()
    print(f"当前进程的父进程编号是：{text1_process_parent_id}")

    while True:
        print("------1")
        time.sleep(1)
        os.kill(text1_process, 9)


def test2():
    # 获取当前进程的编号, 并获取当前进程对象，知道该编号是那个进程的
    test2_process = os.getpid()
    print(f"当前进程的编号: {test2_process}，{multiprocessing.current_process()}")
    # 获取当前的进程的父进程编号
    text2_process_parent_id = os.getppid()
    print(f"当前进程的父进程编号是：{text2_process_parent_id}")
    while True:
        print("------2")
        time.sleep(1)


# 获取当前进程的编号, 并获取当前进程对象，知道该编号是那个进程的
mian_process = os.getpid()
print(f"当前进程的编号: {mian_process}，{multiprocessing.current_process()}")


def main():
    p1 = multiprocessing.Process(target=test1, name="text1_process")
    print(p1)
    p2 = multiprocessing.Process(target=test2, name="text2_process")
    print(p2)
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()