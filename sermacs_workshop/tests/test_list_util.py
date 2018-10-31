"""
Tests for list_util module
"""

import sermacs_workshop as sermacs
import pytest

@pytest.mark.my_test
def test_title_case():
    test_string = "thIs IS a TesT sTrinG"
    title_string = sermacs.title_case(test_string)

    assert title_string == "This Is A Test String"

    return True

def test_type_failure():
    test_input = ['This', 'is', 'a', 'test']

    with pytest.raises(TypeError):
        sermacs.title_case(test_input)

def test_empty_string():
    test_input = ''

    with pytest.raises(IndexError):
        sermacs.title_case(test_input)
