def set_func(func):
    def call_func(a):
        print("-----验证1---")
        print("-----验证2---")
        func(a)
    return call_func


@set_func  # 等价于test1 = set_func(test1)
def test1(num):
    print("----test1----- %d" % num)


@set_func  # 等价于test1 = set_func(test1)
def test2(num):
    print("-----test2---- %d" % num)


# test1 = set_func(test1)
test1(100)
test2(200)