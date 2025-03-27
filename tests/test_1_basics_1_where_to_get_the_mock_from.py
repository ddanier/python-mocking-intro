# We always use the unittest.mock module and import this as `mock`

from unittest import mock


def test_with_unittest_mock():
    some_mock = mock.Mock()

    assert some_mock()
















# DO NOT use the mocker fixture provided my `pytest-mock` and more.

def test_with_pytest_mocker(mocker):  # <- THIS IS BAD
    some_mock = mocker.Mock()

    assert some_mock()
