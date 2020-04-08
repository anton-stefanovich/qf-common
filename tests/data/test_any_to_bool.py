from qf_common.test import pytest_parametrize
from enum import Enum


class TestInput (Enum):
    STRING_JUNK = ['10', '01', '0x', 'Junk', None]
    STRING_TRUE = ['Yes', 'True', 'Y', 'On', '1', 'Enable', 'Enabled']
    STRING_FALSE = ['No', 'False', 'N', 'Off', '0', 'Disable', 'Disabled']


def __check_bool_conversion(*args, reference_value: bool = None, **kwargs):

    from argparse import ArgumentTypeError
    from qf_common.data import any_to_bool

    try:
        result = any_to_bool(*args, **kwargs)

    except ArgumentTypeError:
        assert reference_value is None

    else:
        assert isinstance(result, bool) and \
               result == reference_value


@pytest_parametrize(*TestInput.STRING_TRUE.value)
def test__true_string_to_bool__no_default_value(variant):
    __check_bool_conversion(variant, reference_value=True)


@pytest_parametrize(*TestInput.STRING_TRUE.value)
def test__true_string_to_bool__false_as_default_value(variant):
    __check_bool_conversion(variant, default=False, reference_value=True)


@pytest_parametrize(*TestInput.STRING_FALSE.value)
def test__false_string_to_bool__no_default_value(variant):
    __check_bool_conversion(variant, reference_value=False)


@pytest_parametrize(*TestInput.STRING_FALSE.value)
def test__false_string_to_bool__true_as_default_value(variant):
    __check_bool_conversion(variant, default=True, reference_value=False)


@pytest_parametrize(*TestInput.STRING_JUNK.value)
def test__junk_string_to_bool__no_default_value(variant):
    __check_bool_conversion(variant)


@pytest_parametrize(*TestInput.STRING_JUNK.value)
def test__junk_string_to_bool__true_as_default_value(variant):
    __check_bool_conversion(variant, default=True, reference_value=True)


@pytest_parametrize(*TestInput.STRING_JUNK.value)
def test__junk_string_to_bool__false_as_default_value(variant):
    __check_bool_conversion(variant, default=False, reference_value=False)
