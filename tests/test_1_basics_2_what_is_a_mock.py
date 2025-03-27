from unittest import mock

import pytest


# A mock is a function
def test_mock_is_a_function():
    some_mock = mock.Mock()

    some_mock()

    some_mock.assert_called_once_with()


# A mock has all attributes you could think of
def test_mock_has_attributes():
    some_mock = mock.Mock()

    assert isinstance(some_mock.some_attribute, mock.Mock)


# A mock has all attributes you could think of
def test_mock_attributes_are_function_again():
    some_mock = mock.Mock()

    some_mock.some_method()

    # The attribute will be stored in the mock, so we can access it again
    some_mock.some_method.assert_called_once_with()


# Waaaahhhh....recursion!
def test_mock_attributes_are_function_again_are_function_again_are_function_again_are_function_again():
    some_mock = mock.Mock()

    some_mock.some_attribute.something.i_don_t_care.some_method()

    some_mock.some_attribute.something.i_don_t_care.some_method.assert_called_once_with()


# A mock can use a spec as its basis and will then try to mimic that spec
class Something:
    def some_method(self):
        pass

def test_mock_can_use_spec():
    some_mock = mock.Mock(Something)  # or mock.Mock(spec=Something)

    some_mock.some_method()
    some_mock.some_method.assert_called_once_with()

    with pytest.raises(AttributeError):
        some_mock.some_other_method()
