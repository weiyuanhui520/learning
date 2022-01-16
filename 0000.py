# def funA(fn):
#     # 定义一个嵌套函数
#     def say(arc):
#         print("Python教程:",arc)
#     return say
# @funA
# def funB(arc):
#     print("funB():", a)
# funB("http://c.biancheng.net/python")
# msg=None
from time import time, sleep


def logger(msg=None):
    def run_time(func1):
        def wrapper1(*args, **kwargs):
            start = time()
            func1()  # 函数在这里运行
            end = time()
            cost_time = end - start
            print(msg)
            print("[{}] func three run time {}".format(msg, cost_time))

        return wrapper1

    return run_time


@logger(msg="One")
def fun_one():
    sleep(1)
    print(1)


@logger(msg="Two")
def fun_two():
    sleep(1)
    print(2)


@logger(msg="Three")
def fun_three():
    sleep(1)
    print(3)


fun_one()
fun_two()
fun_three()
