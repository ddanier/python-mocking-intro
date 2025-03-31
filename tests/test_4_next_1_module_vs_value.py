from unittest import mock

import pytest

from mocking_intro.module.receiver import get_answer

# When having some modules and imports the question is: Where to patch/mock things?
#
# See https://docs.python.org/3/library/unittest.mock.html#where-to-patch

@pytest.mark.skip("Will fail, as we are patching the wrong object")
def test_patching_the_original_will_fail():
    with mock.patch("mocking_intro.module.giver.THE_ANSWER", 21):  # Only half of the truth is enough
        assert get_answer() == 21


def test_patching_the_usage_will_work():
    with mock.patch("mocking_intro.module.receiver.THE_ANSWER", 21):  # Only half of the truth is enough
        assert get_answer() == 21















# Reason is that importing something creates a new reference, like with variable assignment

def test_variables_and_references():
    something = 123
    something_else = something

    assert something == 123
    assert something_else == 123

    something = 42

    assert something == 42
    assert something_else == 123  # <- will keep its value















# If you have a magnitured of issues with this....your architecture is BROKEN

def test_patching_all_the_things_is_broken():
    # DON'T DO IT THIS WAY! Your architecture is broken. Introduce some "getter function" instead.
    with (
        mock.patch("mocking_intro.module.giver.THE_ANSWER", 21),
        mock.patch("mocking_intro.module.receiver.THE_ANSWER", 21),
        # mock.patch("mocking_intro.module.somewhere.else.THE_ANSWER", 21),
        # mock.patch("mocking_intro.module.somewhere.else.again.THE_ANSWER", 21),
        # mock.patch("mocking_intro.module.etc.THE_ANSWER", 21),
        # mock.patch("mocking_intro.module.etc.etc.THE_ANSWER", 21),
        # etc...
    ):
        assert get_answer() == 21















# Hint: Importing the module works of course, but may not be suitable for your use case
# (and may hide the architectural issue your code has)

def test_importing_the_module():
    from mocking_intro.module import giver

    with mock.patch("mocking_intro.module.giver.THE_ANSWER", 21):
        assert giver.THE_ANSWER == 21
