import time


class ClassMate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """让一个对象成为一个可以迭代的对象"""
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration


classmate = ClassMate()
classmate.add("张三")
classmate.add("李四")
classmate.add("王五")


for temp in classmate:
    print(temp)
    time.sleep(1)
