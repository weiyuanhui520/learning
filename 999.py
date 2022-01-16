from time import time, sleep


def run_time(func):
    def wrapper():
        start = time()
        func()  # 函数在这里运行
        end = time()
        cost_time = end - start
        print("func three run time {}".format(cost_time))

        # return wrapper


# 111555

@run_time
def fun_one():
    sleep(1)
    print(1)


@run_time
def fun_two():
    sleep(1)
    print(2)


@run_time
def fun_three():
    sleep(1)
    print(3)


fun_one()
