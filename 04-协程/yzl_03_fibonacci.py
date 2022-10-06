class Fibonacci(object):
    """斐伯那契数列"""
    def __init__(self, all_nums):
        self.all_nums = all_nums
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        """让一个对象成为一个可以迭代的对象"""
        return self

    def __next__(self):
        if self.current_num < self.all_nums:
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1
            return ret
        else:
            raise StopIteration


fibo = Fibonacci(10)

for num in fibo:
    print(num)

