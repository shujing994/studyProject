
#单例模式就是，一个类里只能有一个实例，这是一种设计模式，比如说实现的时候只能创造出一个实例对象，不可以重复。

def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]

    return inner


@singleton
class Cls(object):
    def __init__(self):
        pass


cls1 = Cls()
cls2 = Cls()
print(id(cls1) == id(cls2))