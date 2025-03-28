from unittest import mock

import pytest


# You can set the return_value of a mock

def test_return_value():
    some_mock = mock.Mock(return_value="ok")

    assert some_mock() == "ok"
















# This is very useful for more complex mocks

class Inner:
    def some_method(self):
        ...


class Outer:
    def get_inner(self) -> Inner:
        ...


def test_return_value_for_more_complex_case():
    some_mock = mock.Mock(
        Outer,  # <- This is why I prefer to not use `spec=Outer`
        get_inner=mock.Mock(
            return_value=mock.Mock(
                Inner,
                some_method=mock.Mock(return_value="ok"),
            )
        ),
    )

    assert some_mock.get_inner().some_method() == "ok"
















# Of course async mocks work the same

@pytest.mark.anyio
async def test_async_return_value():
    some_mock = mock.AsyncMock(return_value="ok")

    assert await some_mock() == "ok"
