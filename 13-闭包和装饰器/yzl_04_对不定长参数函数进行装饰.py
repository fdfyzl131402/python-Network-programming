def set_func(func):
    def call_func(*args, **kwargs):
        print("-----验证1---")
        print("-----验证2---")
        # func(args, kwargs)  # 相当于传递了两个参数，一个元组，一个字典
        func(*args, **kwargs)  # 拆包

    return call_func


@set_func  # 等价于test1 = set_func(test1)
def test1(num, *args, **kwargs):
    print("----test1----- %d" % num)
    print("----test1----- ", args)
    print("----test1----- ", kwargs)

# test1 = set_func(test1)


test1(100)
test1(100, 200)
test1(100, 200, 300, mm=100)
