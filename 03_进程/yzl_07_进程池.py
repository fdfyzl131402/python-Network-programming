import multiprocessing
import os, time, random


def work(msg):
    start = time.time()
    print("%s进程开始，进程号是%d" % (msg, os.getpid()))
    time.sleep(random.random()*2)
    stop = time.time()
    print(msg,"进程结束，耗时%.2f" % (stop - start))


po = multiprocessing.Pool(3)
for i in range(0, 10):
    po.apply_async(work, (i,))


print("-----start-----")
po.close()
po.join()
print("------end------")