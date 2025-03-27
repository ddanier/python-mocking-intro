from types import GeneratorType
from unittest import mock

import pytest


# Some notes about generators: Result is a generator object!
def some_generator():
    yield 1
    yield 2


def test_return_value_of_generator_is_a_generator():
    result = some_generator()

    assert isinstance(result, GeneratorType)

    for i in result:
        print(i)  # <- prints 1 then 2
















# You can manually collect generators using iter() and next()
# (This is what happends in a for-loop internally)
def test_generators_can_be_collected_with_iter_and_next():
    result = iter(some_generator())

    assert next(result) == 1
    assert next(result) == 2

    # At the end a StopIteration exception is raised
    with pytest.raises(StopIteration):
        next(result)
















# To create a mock for a generator you must return a generator-like object
# see also https://docs.python.org/3/library/unittest.mock-examples.html#mocking-a-generator-method
def test_generators_can_be_mocked():
    generator_mock = mock.Mock(
        return_value=mock.MagicMock(
            __iter__=mock.Mock(side_effect=lambda: iter([1, 2])),  # <- You don't need StopIteration at the end, cause this is the default behaviour
        ),
    )
    result = iter(generator_mock())

    assert next(result) == 1
    assert next(result) == 2

    # At the end a StopIteration exception is raised
    with pytest.raises(StopIteration):
        next(result)
















# Personally I prefer to use a utils function to actually create a generator
def generator(items):
    def _generator():
        yield from items
    return _generator


def test_generators_can_be_mocked_using_utils_function():
    generator_mock = mock.Mock(
        side_effect=generator([1,2]),
    )
    result = iter(generator_mock())

    assert next(result) == 1
    assert next(result) == 2

    # At the end a StopIteration exception is raised
    with pytest.raises(StopIteration):
        next(result)
















# Or a more normal example
def test_generators_can_be_mocked_using_utils_function_in_for():
    generator_mock = mock.Mock(
        side_effect=generator([1,2]),
    )

    result = []
    for i in generator_mock():
        result.append(i)

    assert result == [1, 2]
