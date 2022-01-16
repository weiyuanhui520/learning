import pytest


@pytest.fixture
def first_entry():
    print('aa')
    return "a"


@pytest.fixture
def order(first_entry):
    print(first_entry)
    return [first_entry]


def test_string(order):
    print(order)
    order
    # order.append("b")
    # print (order)
    # assert order == ["a", "b"], "断言执行失败"

    # if __name__ == "__main__":
    #  pytest.main(["test_login.py::test_string", "-s"])
