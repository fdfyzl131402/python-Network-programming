import multiprocessing


def download_from_web(q):
    """下载数据"""
    data = [11, 22, 33, 44]
    # 利用队列写入数据
    for temp in data:
        q.put(temp)
    print("----下载完成----")


def read(q):
    """数据处理"""
    waiting_analysis_date = list()
    # 从队列中获取数据
    while True:
        date = q.get()
        waiting_analysis_date.append(date)

        if q.empty():
            break

    # 模拟数据处理
    print(waiting_analysis_date)


def main():
    # 1.创建队列
    q = multiprocessing.Queue()
    # 2. 创建子进程
    p1 = multiprocessing.Process(target= download_from_web, args=(q,))
    p2 = multiprocessing.Process(target=read, args=(q,))
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()