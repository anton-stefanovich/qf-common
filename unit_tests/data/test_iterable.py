from qf_common.test import pytest_parametrize


@pytest_parametrize(0, 7, -9)
def test_iterable_int(variant):
    from qf_common.data import iterable
    for item in iterable(variant):
        assert isinstance(item, int)


@pytest_parametrize(3.14, -5.79)
def test_iterable_float(variant):
    from qf_common.data import iterable
    for item in iterable(variant):
        assert isinstance(item, float)


@pytest_parametrize(True, False)
def test_iterable_bool(variant):
    from qf_common.data import iterable
    for item in iterable(variant):
        assert isinstance(item, bool)


def test_iterable_single_string():
    from qf_common.data import iterable
    for item in iterable('Single sting'):
        assert isinstance(item, str) and len(item) > 7
