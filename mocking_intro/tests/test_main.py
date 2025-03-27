from mocking_intro.main import root

def test_main():
    assert root() == {"Hello": "World"}
