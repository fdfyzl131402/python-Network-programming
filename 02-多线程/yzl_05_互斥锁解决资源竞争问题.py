import threading
import time

g_num = 0


def test1(num):
    # 上锁
    mutex.acquire()
    global g_num
    for i in range(num):
        g_num += 1
    # 解锁
    mutex.release()
    print("------test1---%d--" % g_num)


def test2(num):
    mutex.acquire()
    global g_num
    for i in range(num):
        g_num += 1
    mutex.release()
    print("------test2---%d--" % g_num)


# 创建一个互斥锁，默认是解锁的
mutex = threading.Lock()


def main():
    t1 = threading.Thread(target=test1, args=(10000000,))
    t2 = threading.Thread(target=test2, args=(10000000,))
    t1.start()
    t2.start()
    time.sleep(2)
    print("in main thread g_nums = %d" % g_num)


if __name__ == "__main__":
    main()