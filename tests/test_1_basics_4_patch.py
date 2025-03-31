from unittest import mock

import pytest


# You may use `mock.patch` to replace any foreign module attribute
#
# See ../mocking_intro/functions.py

@pytest.fixture
def mock_production_code():
    with mock.patch("mocking_intro.functions.production_code") as mocked:
        yield mocked  # <- Needs to be yielded


def run_this():
    from mocking_intro.functions import production_code

    production_code()


@pytest.mark.skip("This will raise an execption, as we didn't mock the production code")
def test_production_code_will_be_executed_without_mock():
    run_this()


def test_production_code_will_be_mocked_by_patch(mock_production_code):
    run_this()

    mock_production_code.assert_called_once_with()
















# You may use `autospec=True` to grab the spec before the patch
#
# See ../mocking_intro/classes.py
# Note: `patch` will use `MagicMock` or `AsyncMock` depending on the object type it needs to patch

@pytest.fixture
def mock_production_class():
    with mock.patch("mocking_intro.classes.ProductionClass", autospec=True) as mocked:
        yield mocked  # <- Needs to be yielded


def test_production_class_spec_will_be_used(mock_production_class):
    mock_production_class.do_something()

    mock_production_class.do_something.assert_called_once_with()


@pytest.mark.skip("This will raise an AttributeError, as non_existing_method is not part of spec")
def test_production_class_spec_will_disallow_misuse(mock_production_class):
    mock_production_class.non_existing_method()
