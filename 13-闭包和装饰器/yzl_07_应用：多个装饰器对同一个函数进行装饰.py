def set_func_1(func):
    def call_func():
        return "<td>" + func() + "</td>"
    return call_func


def set_func_2(func):
    def call_func():
        return "<h5>" + func() + "</h5>"
    return call_func


@set_func_1
@set_func_2
def test():
    return "haha"


print(test())
