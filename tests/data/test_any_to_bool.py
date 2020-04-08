from src.test import pytest_parametrize
from enum import Enum


class TestInput (Enum):
    STRING_JUNK = ['10', '01', '0x', 'Junk', None]
    STRING_TRUE = ['Yes', 'True', 'Y', 'On', '1', 'Enable', 'Enabled']
    STRING_FALSE = ['No', 'False', 'N', 'Off', '0', 'Disable', 'Disabled']


def __check_bool_conversion(variant: any, is_positive_test: bool, reference_value: bool = None):
    from argparse import ArgumentTypeError
    from src.data import any_to_bool

    try:
        result = any_to_bool(variant)

    except ArgumentTypeError:
        assert not is_positive_test

    else:
        assert is_positive_test and \
               isinstance(result, bool) and \
               result == reference_value


@pytest_parametrize(*TestInput.STRING_TRUE.value)
def test_true_string_to_bool(variant):
    __check_bool_conversion(variant, is_positive_test=True, reference_value=True)


@pytest_parametrize(*TestInput.STRING_FALSE.value)
def test_false_string_to_bool(variant):
    __check_bool_conversion(variant, is_positive_test=True, reference_value=False)


@pytest_parametrize(*TestInput.STRING_JUNK.value)
def test_junk_string_to_bool(variant):
    __check_bool_conversion(variant, is_positive_test=False)
