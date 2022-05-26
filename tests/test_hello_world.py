from src.hello_world import HelloWorld


def test_hello_world___call__():
    obj = HelloWorld()
    result = obj()
    assert list(result.size()) == [5, 3]