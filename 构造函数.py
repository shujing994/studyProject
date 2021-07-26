# 我们在Python当中怎么实现单例(Singleton)的设计模式呢？
# 从这个问题出发，你会发现只使用__init__函数是不可能完成的，因为__init__并不是构造函数，它只是初始化方法。

class Student:

    def __new__(cls, *args, **kwargs):
        print("我是构造函数")
        return object.__new__(cls)

    def __init__(self, name, score):
        print("我是初始化方法")
        self.name = name
        self.score = score

    def get_score(self):
        return "我是" + self.name + ",分数" + str(self.score)


student = Student("小明", 98)
print(student.get_score())
