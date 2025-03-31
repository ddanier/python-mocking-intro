import contextlib
from unittest import mock

import pytest


# A context manager is an object that implements __enter__ and __exit__
#
# See https://docs.python.org/3/reference/compound_stmts.html#with

class SimpleContextManager:
    did_call_enter = False
    did_call_exit = False

    def __enter__(self):
        self.did_call_enter = True
        return "something"

    def __exit__(self, exc_type, exc_value, traceback):
        self.did_call_exit = True


def test_simple_context_manager():
    content_manager = SimpleContextManager()

    assert content_manager.did_call_enter is False
    assert content_manager.did_call_exit is False

    with content_manager as context:
        assert context == "something"
        assert content_manager.did_call_enter is True
        assert content_manager.did_call_exit is False

    assert content_manager.did_call_enter is True
    assert content_manager.did_call_exit is True
















# However: Normally I would recommend using the content manager decorators instead.

@contextlib.contextmanager
def simple_context_manager():
    yield "something"


def test_simple_context_manager_using_decorator():
    content_manager = simple_context_manager()

    with content_manager as context:
        assert context == "something"
















# But for mocking we can use a mock implementing those two methods

def test_simple_context_manager_mock():
    content_manager_mock = mock.Mock(
        __enter__=mock.Mock(return_value="something"),
        __exit__=mock.Mock(),
    )

    content_manager_mock.__enter__.assert_not_called()
    content_manager_mock.__exit__.assert_not_called()

    with content_manager_mock as context:
        assert context == "something"
        content_manager_mock.__enter__.assert_called_once()
        content_manager_mock.__exit__.assert_not_called()

    content_manager_mock.__enter__.assert_called_once()
    content_manager_mock.__exit__.assert_called_once()
















# Same is true for async context managers (although naming changes)
#
# See https://docs.python.org/3/reference/compound_stmts.html#the-async-with-statement

@pytest.mark.anyio
async def test_async_content_manager():
    content_manager_mock = mock.Mock(
        __aenter__=mock.AsyncMock(return_value="something"),  # <- async version now
        __aexit__=mock.AsyncMock(),
    )

    content_manager_mock.__aenter__.assert_not_awaited()
    content_manager_mock.__aexit__.assert_not_awaited()

    async with content_manager_mock as context:
        assert context == "something"
        content_manager_mock.__aenter__.assert_awaited_once()
        content_manager_mock.__aexit__.assert_not_awaited()

    content_manager_mock.__aenter__.assert_awaited_once()
    content_manager_mock.__aexit__.assert_awaited_once()
