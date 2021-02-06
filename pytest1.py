import pytest


# class Test_ABC:
#     def setup_class(self):
#         print("------->setup_class")
#     def teardown_class(self):
#         print("------->teardown_class")
#     def test_a(self):
#         print("------->test_a")
#         assert 1
#     @pytest.mark.skipif(condition=2 > 1, reason ="跳过该函数") # 跳过测试函数test_b
#     def test_b(self):
#         print("------->test_b")
#         assert 0

def setup_module():
    print('setup_fuc')


def teardown_module():
    print('teardown_fuc')


def test_fuc():
    print('test_fuc1')


def test_fuc2():
    print('test_fuc2')


class Test_ABC:
    def setup_method(self):
        print("------->setup_class")

    def teardown_method(self):
        print("------->teardown_class")

    def test_a(self):
        print("------->test_a")
        assert 1

    @pytest.mark.xfail(2 > 1, reason="标注为预期失败")  # 标记为预期失败函数test_b
    def test_b(self):
        print("------->test_b")
        assert 0


pytest.main(["-s", "pytest1.py"])
