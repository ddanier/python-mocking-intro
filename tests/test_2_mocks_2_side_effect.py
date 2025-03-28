from unittest import mock

import pytest


# You can use a side_effect to raise exceptions

def test_side_effect_for_exceptions():
    some_mock = mock.Mock(side_effect=RuntimeError)

    with pytest.raises(RuntimeError):
        some_mock()
















# You can use a side_effect to execute any code

def test_side_effect_for_code():
    some_mock = mock.Mock(side_effect=lambda: 1 + 1)  # <- can also be functions defined elsewhere

    assert some_mock() == 2
















# You can use a side_effect to return different values of subsequent calls

def test_side_effect_with_list():
    some_mock = mock.Mock(side_effect=[1,2,3])

    assert some_mock() == 1
    assert some_mock() == 2
    assert some_mock() == 3

    # WARNING: This will trigger an error at the end
    with pytest.raises(StopIteration):
        assert some_mock() == 1
