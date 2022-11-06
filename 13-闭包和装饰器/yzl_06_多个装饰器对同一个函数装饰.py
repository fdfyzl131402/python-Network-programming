def add_power(func):
    print("----装饰器验证1----")

    def call_func(*args, **kwargs):
        print("-----验证1---")
        return func(*args, **kwargs)
    return call_func


def add_project(func):
    print("----装饰器验证2----")

    def call_func(*args, **kwargs):
        print("-----验证2---")
        return func(*args, **kwargs)
    return call_func


@add_power
@add_project  # 等价于test1 = add_project(test1)
# 此处先装饰第二个，在装第一个，但先打印第一个，在打印第二个，相当于函数嵌套
def test1():
    print("----test1----")

# test1 = set_func(test1)


test1()
