def fibo(all_nums):
    a, b = 0, 1
    current_nums = 0
    while current_nums < all_nums:
        a, b = b, a+b
        ret = yield a
        print("--ret--", ret)
        current_nums += 1


obj = fibo(10)

ret = next(obj)
print(ret)

ret = obj.send("hahaha")
print(ret)