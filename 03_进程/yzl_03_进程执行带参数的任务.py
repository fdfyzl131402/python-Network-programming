import multiprocessing


def main(name, age):
    print(name, age)


# sub_process = multiprocessing.Process(target=main, args=("张三", 20))
# sub_process.start()

# sub_process = multiprocessing.Process(target=main, kwargs={"age":20, "name": "wangwu"})
# sub_process.start()

sub_process = multiprocessing.Process(target=main, args=("wangwu",), kwargs={"age": 20})
sub_process.start()