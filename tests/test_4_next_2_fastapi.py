from unittest import mock

import pytest
from fastapi import FastAPI
from httpx import AsyncClient, ASGITransport


# You can (and should) use the httpx async client for testing
#
# See ../mocking_intro/fastapi/main.py
# Note: The FastAPI docs use fastapi.testclient.TestClient in sync tests. This may create issues with
#       the anyio async handling with async fixtures. I recommend always using the httpx AsyncClient
#       instead.
#       References:
#        * TestClient: https://fastapi.tiangolo.com/tutorial/testing/#using-testclient
#        * AsyncClient from httpx: https://fastapi.tiangolo.com/advanced/async-tests/#example
# Note: This is not a unit test as of now - more on mocking later.

@pytest.mark.anyio
async def test_root():
    from mocking_intro.fastapi.main import app

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url='http://test',
    ) as client:
        response = await client.get("/")

        assert response.status_code == 200















# The app itself should be put into a fixture to avoid loading the ap when collecting the tests
#
# Note: This means pytest will be able to start the tests faster and then (late) load the app during the tests.
#       For bigger projects this will increase the startup of pytest significantly. This is especially useful
#       if your only run parts of the tests.
# Note: Also the client should be put into a fixture.
# Note: This is still not a unit test.

@pytest.fixture(scope="session")  # <- session scope should be just fine here
def app():
    from mocking_intro.fastapi.main import app

    return app


@pytest.fixture
async def app_client(app):
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url='http://test',
    ) as client:
        yield client


@pytest.mark.anyio
async def test_root_with_app_fixture(app_client):
    response = await app_client.get("/")

    assert response.status_code == 200















# Now let's introduce some mocking to ensure we have a unit test.
#
# See ../mocking_intro/fastapi/main.py
# See ../mocking_intro/fastapi/routes/answer.py
# Note: This means that mocking in FastAPI is nothing special - just normal mocking as always.
# Note: Compare those two commands to see the difference:
#       uv run pytest --cov mocking_intro/ tests/test_4_next_2_fastapi.py::test_root_with_app_fixture
#       uv run pytest --cov mocking_intro/ tests/test_4_next_2_fastapi.py::test_root_as_unit_test
#       (Hint: Look at the coverage of mocking_intro/module/receiver.py)
# Warning: Still not strictly a unit test.

@pytest.mark.anyio
async def test_root_as_unit_test(app_client):
    with mock.patch("mocking_intro.fastapi.routes.answer.get_answer", return_value=21):
        response = await app_client.get("/answer/")

    assert response.status_code == 200
    assert response.json()["answer"] == 21















# Still we don't really have a unit test, as this all depends on the main FastAPI app. The answer router
# is integrated into this. So let's create a real unit.
#
# Hint: Also do this when you test dependencies etc. This allows you to ensure a) you have a well defined
#       test case and b) allows you to also test for and thus support different configurations etc.

@pytest.fixture(scope="session")
def answer_app():
    from mocking_intro.fastapi.routes.answer import router

    app = FastAPI()
    app.include_router(router)

    return app


@pytest.fixture
async def answer_app_client(answer_app):
    async with AsyncClient(
        transport=ASGITransport(app=answer_app),
        base_url='http://test',
    ) as client:
        yield client


@pytest.mark.anyio
async def test_answer_app(answer_app_client):
    with mock.patch("mocking_intro.fastapi.routes.answer.get_answer", return_value=21):
        response = await answer_app_client.get("/")  # <- URL is now relative to router

    assert response.status_code == 200
    assert response.json()["answer"] == 21
