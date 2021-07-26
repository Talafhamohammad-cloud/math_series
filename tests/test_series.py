from math_series.series import fibo
from math_series.series import lucas
from math_series.series import sum_series


def test_fibonacci_5():
    assert fibo(5) == 5


def test_fibonacci_2():
    assert fibo(2) == 1


def test_fibonacci_3():
    assert fibo(3) == 2


def test_fibonacci_7():
    assert fibo(7) == 13


def test_lucas_0():
    assert lucas(0) == 2


def test_lucas_3():
    assert lucas(3) == 4


def test_lucas_7():
    assert lucas(7) == 29


def test_sum_series():
    assert sum_series(3, 4, 2) == 8


def test_sum_series():
    assert sum_series(3,5,1)==7
