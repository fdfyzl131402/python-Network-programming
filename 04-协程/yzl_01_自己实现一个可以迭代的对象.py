import time
from collections.abc import Iterable
from collections.abc import Iterator


class ClassMate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """让一个对象成为一个可以迭代的对象"""
        return ClassIterator(self)


class ClassIterator(object):
    def __init__(self, obj):
        self.obj = obj
        self.current_num = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.current_num < len(self.obj.names):
            ret = self.obj.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration


classmate = ClassMate()
classmate.add("张三")
classmate.add("李四")
classmate.add("王五")
# print("判断classmate是否可以迭代：", isinstance(classmate, Iterable))
# classmate_Iterator = iter(classmate)
# print("判断classmate_Iterator是否是迭代器：", isinstance(classmate_Iterator, Iterator))

for temp in classmate:
    print(temp)
    time.sleep(1)
