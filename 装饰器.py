# 当你把一对小括号放在后面，这个函数就会执行；
# 然而如果你不放括号在它后面，那它可以被到处传递，并且可以赋值给别的变量而不去执行它。


def greet(abc):
    def greet_str(name):
        if (name == "阿赟"):
            return name + abc()
        else:
            return name + "不" + abc()
    return greet_str


@greet
def love():
    return "可以进阿靖靖房间"

# @greet 相当于在定义函数后执行了一条语句， love = greet(love)
# love = greet(love)


print(love("阿赟"))
print(love("阿shazi"))


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         """doc of wrapper"""
#         print('123')
#         return func(*args, **kwargs)
#
#     return wrapper
#
# # @decorator
# def say_hello():
#     """doc of say hello"""
#     print('同学你好')
#
# say_hello = decorator(say_hello)
#
# print(say_hello.__name__)
# print(say_hello.__doc__)

