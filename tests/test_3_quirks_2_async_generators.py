from types import AsyncGeneratorType
from unittest import mock

import pytest


# Async generators also return a generator object, a AsyncGenerator in this case
async def some_generator():
    yield 1
    yield 2


@pytest.mark.anyio
async def test_return_value_of_async_generator_is_an_async_generator():
    result = some_generator()  # <- NO await

    assert isinstance(result, AsyncGeneratorType)

    async for i in result:  # <- async for needed
            print(i)  # <- prints 1 then 2















# You can manually collect async generators using aiter() and anext()
# (This is what happends in a for-loop internally)
@pytest.mark.anyio
async def test_async_generators_can_be_collected_with_iter_and_next():
    result = aiter(some_generator())  # <- still NO await


    assert await anext(result) == 1  # <- THIS is where the await is happening
    assert await anext(result) == 2

    # At the end a StopAsyncIteration exception is raised
    with pytest.raises(StopAsyncIteration):
        await anext(result)
















# Let's use the util function schema to create a async generator mock
# (Note: Mocking this using only mocks is really hard - I would just not do this)
def async_generator(items):
    async def _generator():
        for item in items:  # <- There is no `async yield from`, see https://peps.python.org/pep-0525/#asynchronous-yield-from
            yield item
    return _generator


@pytest.mark.anyio
async def test_async_generators_can_be_mocked_using_utils_function():
    generator_mock = mock.Mock(  # <- This is NOT a AsyncMock, as explained above
        side_effect=async_generator([1,2]),
    )
    result = aiter(generator_mock())

    assert await anext(result) == 1
    assert await anext(result) == 2

    # At the end a StopAsyncIteration exception is raised
    with pytest.raises(StopAsyncIteration):
        await anext(result)
















# Or a more normal example
@pytest.mark.anyio
async def test_async_generators_can_be_mocked_using_utils_function_in_for():
    generator_mock = mock.Mock(
        side_effect=async_generator([1,2]),
    )

    result = []
    async for i in generator_mock():
        result.append(i)

    assert result == [1, 2]
