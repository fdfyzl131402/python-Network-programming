import gevent
import time
from  gevent import monkey
# 所有耗时操作和堵塞操作都要用gevent中的模块，例如 socket中的recv 和 connect time里面的sleep
# 但这样太麻烦，因此用monkey模块
monkey.patch_all()  # 程序中需要用耗时的操作都用 gevent中的sleep


def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)
        # gevent.sleep(0.5)


def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)
        # gevent.sleep(0.5)


def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)
        # gevent.sleep(0.5)


# 此处四个打印任务都会同时进行完， 因为下面的创建对象不是耗时操作，所以会进行完
print("---1----")
# g1 = gevent.spawn(f1, 5)
print("---2---")
# g2 = gevent.spawn(f2, 5)
print("---3----")
# g3 = gevent.spawn(f3, 5)
print("---4----")
# 耗时操作
# g1.join()
# g2.join()
# g3.join()
# 代替上面更简洁
gevent.joinall([
    gevent.spawn(f1, 5),
    gevent.spawn(f2, 5),
    gevent.spawn(f3, 5)

])
