from unittest import mock

import mock_open
import pytest


# You may use unittest.mock.mock_open to create a mock for opening files
#
# See: https://docs.python.org/3/library/unittest.mock.html#mock-open

def test_file_open():
    with mock.patch(
        "builtins.open",  # <- override/patch global open function
        mock.mock_open(read_data="Hello world"),  # <- mock_open provides the mock in this case
    ):
        with open("some_file_name.i_dont_care", "r") as fh:
            assert fh.read() == "Hello world"















# You can also use the mackage mock-open to actually mock a whole filesystem.
#
# See: https://pypi.org/project/mock-open/

def test_mock_open():
    open_mock = mock_open.MockOpen()
    open_mock["/hello-world.txt"].read_data = "Hello world"
    open_mock["/broken-file.txt"].side_effect = RuntimeError

    with mock.patch(
        "builtins.open",
        open_mock,  # <- Use the open_mock in this case, as it mocks both files differently
    ):
        with open("/hello-world.txt", "r") as fh:
            assert fh.read() == "Hello world"

        with pytest.raises(RuntimeError):
            open("/broken-file.txt")
