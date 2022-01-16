import pytest


# 定义的夹具函数，使用装饰器pytest.fixture
@pytest.fixture(scope='class')
def my_fruit():
    print("login:用户执行登录操作")


# 使用夹具函数的测试用例
def test_my_fruit_in_basket(my_fruit):
    print("hello world")


def test_my_fruit_in_basket2(my_fruit):
    print("hello world222")


class Test_LX():
    def test_my_fruit_in_basket_class(self, my_fruit):
        print("hello world_class01")

    def test_my_fruit_in_basket_class02(self, my_fruit):
        print("hello world_class02")


if __name__ == '__main__':
    # pytest.main(['test_login.py::test_my_fruit_in_basket', '-s'])
    pytest.main(['test_login.py', '-v'])
