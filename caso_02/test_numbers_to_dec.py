import pytest

from numbers_to_dec import list_to_decimal

# [0, 4, 2, 8] => 428
# [1, 2] => 12
# [3] => 3
# [6, 2, True] => raises TypeError
# [-3, 12] => raises ValueError
# [3.6, 4, 1] => raises TypeError
# ['4', 5, 3, 1] => raises TypeError

# write one or more pytest functions below, they need to start with test_
# @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
# def test_eval(test_input, expected):
#    assert eval(test_input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ([1, 2, 3], 123),
        ([0, 0, 0, 4], 4),
        ([3], 3),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 1234567890),
    ],
)
def test_valores_validos(input, expected):
    assert list_to_decimal(input) == expected


def test_valores_type_error():
    with pytest.raises(TypeError):
        list_to_decimal([True])
        list_to_decimal([3.2])
        list_to_decimal(["ola ke ase"])


def test_valores_value_error():
    with pytest.raises(ValueError):
        list_to_decimal([1, 2, 10])
        list_to_decimal([15, 1, 2])
        list_to_decimal([0, 0, 1000])
        list_to_decimal([-3, -10])
        list_to_decimal([11])
        list_to_decimal([-10, -12])
        list_to_decimal([10, 12])
        list_to_decimal([1, 2, 80])
        list_to_decimal([10, 1, 2])
        list_to_decimal([0, -4, 2, 8])
        list_to_decimal([10, 4, 2, 8])
        list_to_decimal([1, -2])
        list_to_decimal([-10, -2])
        list_to_decimal([-3])
        list_to_decimal([1, 4, 2, 80])
        list_to_decimal([11])
