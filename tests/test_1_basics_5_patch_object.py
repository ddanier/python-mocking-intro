from unittest import mock


# `mock.patch.object` can be used to patch object instance attributes

class Something:
    attr = "Und alle so Yeah!"


def test_mock_patch_object_replaces_attribute():
    something = Something()

    with mock.patch.object(something, "attr", "new value"):
        assert something.attr == "new value"

    assert something.attr == "Und alle so Yeah!"
















# `mock.patch.multiple` patches multiple attributes

class SomethingElse:
    attr1 = 1
    attr2 = 2


def test_mock_patch_multiple_patches_multiple_things():
    something = SomethingElse()

    with mock.patch.multiple(something, attr1=23, attr2=42):
        assert something.attr1 == 23
        assert something.attr2 == 42

    assert something.attr1 == 1
    assert something.attr2 == 2
















# Note: There also is a `mock.patch.dict` function (I never use this....)

def test_mock_patch_dict_replaces_item():
    somedict = {"hello": "world"}

    with mock.patch.dict(somedict, {"hello": "peter"}):
        assert somedict["hello"] == "peter"

    assert somedict["hello"] == "world"
