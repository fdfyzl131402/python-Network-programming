def set_level(level_num):
    def set_func(func):
        def call_func(*args, **kwargs):
            if level_num == 1:
                print("----验证测试1----")
            elif level_num == 2:
                print("----验证厕所2----")
            return func()
        return call_func
    return set_func


# 调用set_func并将1作为实参传入
# 用上一步的返回值当作装饰器对test1进行装饰
@set_level(1)
def test1():
    print("----test1----")
    return "ok"


@set_level(2)
def test2():
    print("----test2----")
    return "ok"


test1()
test2()
