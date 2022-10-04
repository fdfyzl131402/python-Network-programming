import multiprocessing
import time


def task():
    while True:
        print("任务进行中...")
        time.sleep(0.2)


def main():
    sub_process = multiprocessing.Process(target=task)
    # sub_process.daemon = True
    sub_process.start()

    time.sleep(1)
    # 在主进程结束之前先让子进程销毁
    sub_process.terminate()
    print("over")
    # 主进程会等待子进程完成再销毁
    # 解决办法：1.让子进程成为守护主进程， 主进程退出子进程销毁，子进程会依赖主进程
    # 2. 让主进程退出之前先让子进程销毁


if __name__ == "__main__":
    main()