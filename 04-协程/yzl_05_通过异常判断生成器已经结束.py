def fibo(all_nums):
    a, b = 0, 1
    current_nums = 0
    while current_nums < all_nums:
        yield a  # 如果一个函数有yield ，那么这个函数变成了一个生成器'
        a, b = b, a+b
        current_nums += 1
        return "over"


obj2 = fibo(20)

while True:
    try:
        ret = next(obj2)
        print(ret)
    except Exception as ret:
        print(ret.value)
        break