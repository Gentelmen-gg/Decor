# def test():
#     print(hello)
#
# x = test()
# x2 = print
#
# x2("hello welcome")
# print("data")

# def test_decor(func):
#     return func
#
#
# def test():
#     return "hello"
#
#
# x = test_decor(test)
# print((x))

# def test_decor(func):
#     return func
#
# @test_decor
# def test():
#     return "hello"
#
# print(test())
import time

def txt_upper(func):
    def wrapper():
        x = func
        print("Эта функция возвращает - ", func())
    return wrapper

@txt_upper
def test2():
    return "hello"


test2()
