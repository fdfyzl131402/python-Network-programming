import time


def task_01():
    while True:
        print("----1----")
        time.sleep(0.1)
        yield


def task_02():
    while True:
        print("----2----")
        time.sleep(0.1)
        yield


def main():
    t1 = task_01()
    t2 = task_02()
    while True:
        next(t1)
        next(t2)


if __name__ == "__main__":
    main()