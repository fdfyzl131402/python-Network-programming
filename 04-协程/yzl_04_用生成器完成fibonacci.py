def fibo(all_nums):
    """使用print 调试来判断使用yield后生成器是怎么执行的"""
    print("-----1-----")
    a, b = 0, 1
    current_nums = 0
    while current_nums < all_nums:
        print("----2----")
        yield a  # 如果一个函数有yield ，那么这个函数变成了一个生成器'
        print("------3------")
        a, b = b, a+b
        current_nums += 1
        print("----4----")


obj = fibo(10)
obj2 = fibo(2)  # 这两个不会相互影响

ret = next(obj)
print(ret)

ret = next(obj)
print(ret)

ret = next(obj2)
print(ret)

ret = next(obj)
print(ret)

ret = next(obj)
print(ret)

ret = next(obj)
print(ret)
# for num in obj:
#     print(num)
