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


@pytest.mark.parametrize(
    "arg, expected", [([0, 4, 2, 8], 428), ([1, 2], 12), ([3, 5, 1], 351)]
)
def test_valid_input(arg, expected):
    assert list_to_decimal(arg) == expected


def test_value_error_lt_min():
    with pytest.raises(ValueError):
        list_to_decimal([-3, 2, 1])


def test_value_error_gt_max():
    with pytest.raises(ValueError):
        list_to_decimal([2, 1, 10])


def test_type_error_str():
    with pytest.raises(TypeError):
        list_to_decimal(["str", 2, 1])


def test_type_error_float():
    with pytest.raises(TypeError):
        list_to_decimal([1, 2, 3.6])
