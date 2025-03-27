import json
from unittest import mock

# Unit tests only run code in one unit (function or file ....or module)

def unit():
    return True

def test_unit():
    assert unit() is True














# Integration tests will ensure the interface between units work

def other_unit():
    return True

def integration():
    return unit() and other_unit()

def test_integration():
    assert integration() is True
















# End to end tests will check the whole setup
# (note: for FE would start up a browser)

def e2e():
    # Normally would use some test client for example
    api_result = f'{{"result": {json.dumps(integration())}}}'
    return json.loads(api_result)

def test_e2e():
    assert e2e()["result"] is True
