import pytest

from mocking_intro.main import root


@pytest.mark.anyio
async def test_main():
    assert await root() == {"Hello": "World"}
