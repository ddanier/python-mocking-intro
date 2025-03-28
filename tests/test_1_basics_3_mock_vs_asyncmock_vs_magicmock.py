from unittest import mock

import pytest


# A mock will not allow async usage by default

@pytest.mark.anyio
async def test_mock_is_not_async():
    some_mock = mock.Mock()

    with pytest.raises(TypeError):
        await some_mock()
















# But you can create async mocks

@pytest.mark.anyio
async def test_asyncmock_is_async():
    some_mock = mock.AsyncMock()

    await some_mock()

    some_mock.assert_awaited_once_with()
















# Be sure to use "awaited" assertions

@pytest.mark.anyio
async def test_asyncmock_needs_to_be_awaited():
    some_mock = mock.AsyncMock()

    coroutine = some_mock()

    some_mock.assert_called_once_with()
    some_mock.assert_not_awaited()  # <- This may be a bug in your code!

    await coroutine

    some_mock.assert_called_once_with()
    some_mock.assert_awaited_once_with()
















# Async methods with a spec don't need an AsyncMock

class Something:
    async def some_method(self):
        pass


@pytest.mark.anyio
async def test_asyncmock_for_spec():
    some_mock = mock.Mock(Something)  # <- NO need for AsyncMock here!

    await some_mock.some_method()

    some_mock.some_method.assert_awaited_once_with()
















# If you would use an AsyncMock the mock itself would be async

@pytest.mark.anyio
async def test_asyncmock_for_spec_WRONG():
    some_mock = mock.AsyncMock(Something)  # <- THIS IS WRONG

    await some_mock()  # <- Unless you do this, BUT WHY???!
















# Magic mocks are when using magic methods (and a spec)
#
# Note: Python will use MagicMock by default, to ensure maximum compatibility, see `patch` later.
# Note: More about context managers later!

class SomeContextManager:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass


@pytest.mark.skip("Without the MagicMock __enter__ and __exit__ won't exist")
def test_magic_methods_dont_exist_on_normal_mock():
    some_mock = mock.Mock(SomeContextManager)

    with some_mock:
        pass


def test_magic_methods_do_exist_on_magic_mock():
    some_mock = mock.MagicMock(SomeContextManager)

    with some_mock:
        pass
