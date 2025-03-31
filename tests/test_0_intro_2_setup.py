import pytest


# We use anyio, as it has the cleanest way to support async + is what FastAPI uses anyways
# (Hint: conftest.py)

async def something():
    return {"Hello": "World"}


@pytest.mark.anyio
async def test_main():
    assert await something() == {"Hello": "World"}
















# With anyio an async fixture will only be awaited if your test is async

@pytest.fixture
async def async_fixture():
    return True


@pytest.mark.anyio
async def test_fixture_in_async_test(async_fixture):
    assert async_fixture is True


@pytest.mark.skip("This will fail, as async_fixture is a coroutine now")
def test_fixture_in_sync_test(async_fixture):
    assert async_fixture is True
