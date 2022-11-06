# def set_func_1(func):
#     def call_func():
#         return "<td>" + func() + "</td>"
#     return call_func


class Test(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("装饰器添加的功能")
        return self.func()


@Test  # 相当于test= Test(test)
def test():
    return "haha"


print(test())
