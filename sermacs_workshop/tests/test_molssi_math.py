"""
Tests for molssi_math module
"""

import sermacs_workshop as sermacs
import pytest

@pytest.fixture
def num_list_3():
    return [1, 2, 3, 4, 5]

@pytest.mark.parametrize("num_list, expected_mean", [
([1, 2, 3, 4, 5], 3.0),
([0, 2, 4, 6], 3),
([1, 2, 3, 4], 2.5)
])

def test_many(num_list, expected_mean):
    assert sermacs.mean(num_list) == expected_mean

def test_numeric_input():
    num_list = [1, 'a', 'b']

    with pytest.raises(TypeError):
        sermacs.mean(num_list)

def test_input_type():
    test_input = ''

    with pytest.raises(TypeError):
        sermacs.mean(test_input)

def test_zero_length():
    num_list = []

    with pytest.raises(ZeroDivisionError):
        sermacs.mean(num_list)

def test_mean(num_list_3):
    assert sermacs.mean(num_list_3) == 3.0

@pytest.mark.parametrize("x", [0,1])
@pytest.mark.parametrize("y", [2,3])

def test_foo(x, y):
    pass
