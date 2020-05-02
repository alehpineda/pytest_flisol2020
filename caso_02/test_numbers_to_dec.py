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
