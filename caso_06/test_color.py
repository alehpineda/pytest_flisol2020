from unittest.mock import patch

import pytest

import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()

# write one or more pytest functions below, they need to start with test_
