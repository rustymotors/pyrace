from pyrace.gateway.parseQuery import parseQuery


def test_parseQuery():
    # Test case 1: Empty path
    path = ""
    expected_result = {}
    assert parseQuery(path) == expected_result

    # Test case 2: Path without query parameters
    path = "/example"
    expected_result = {}
    assert parseQuery(path) == expected_result

    # Test case 3: Path with single query parameter
    path = "/example?param1=value1"
    expected_result = {"param1": "value1"}
    assert parseQuery(path) == expected_result

    # Test case 4: Path with multiple query parameters
    path = "/example?param1=value1&param2=value2&param3=value3"
    expected_result = {"param1": "value1", "param2": "value2", "param3": "value3"}
    assert parseQuery(path) == expected_result

    # Test case 5: Path with query parameter containing special characters
    path = "/example?param1=value1&param2=value%20with%20spaces"
    expected_result = {"param1": "value1", "param2": "value%20with%20spaces"}
    assert parseQuery(path) == expected_result
