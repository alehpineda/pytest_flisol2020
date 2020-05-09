from fibonacci import fib
import pytest


# write one or more pytest functions below, they need to start with test_
def test_valor():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3


def test_value_error():
    with pytest.raises(ValueError) as excinfo:
        fib(-1)
    assert "Error. Ingresa un numero positivo." in str(excinfo.value)
