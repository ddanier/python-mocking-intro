import random
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
















# A mock can also use an instance as its spec

def test_mock_can_use_instance_spec():
    instance = Something()
    some_mock = mock.Mock(instance)  # or mock.Mock(spec=instance)

    some_mock.some_method()
    some_mock.some_method.assert_called_once_with()

    with pytest.raises(AttributeError):
        some_mock.some_other_method()
















# The spec will not forbid the mock itself being callable (mocking classes)

def test_mock_with_spec_is_still_callable():
    SomeMock = mock.Mock(Something)  # or mock.Mock(spec=Something)

    x = SomeMock()
    x.some_method()

    # Use the return value when you do something like this
    SomeMock.return_value.some_method.assert_called_once_with()

    # But note: The return value will just be a plain mock by default
    x.some_other_method()  # <- Will not fail in this case

    # More on return values later!
















# You can also check the arguments of a call

def test_mock_can_check_arguments():
    some_mock = mock.Mock()

    some_mock(1, 2, 3)
    some_mock.assert_called_once_with(1, 2, 3)

    # You may also check for subsequent calls
    some_mock(4, 5, 6)
    some_mock.assert_has_calls([
        mock.call(1, 2, 3),
        mock.call(4, 5, 6)
    ])  # or use any_order=True

    # You may reset the mock, if will then forget all calls
    some_mock.reset_mock()

    # You may use mock.ANY if you don't care about arguments
    some_mock(1, 2, random.randint(0, 10))
    some_mock.assert_called_once_with(1, 2, mock.ANY)
















# You can of course also check for keyworded arguments

def test_mock_can_check_keyworded_arguments():
    some_mock = mock.Mock()

    some_mock(1, 2, c=3)
    some_mock.assert_called_once_with(1, 2, c=3)

    # But note the assertion must REALLY match
    with pytest.raises(AssertionError):
        some_mock.assert_called_once_with(1, 2, 3)
