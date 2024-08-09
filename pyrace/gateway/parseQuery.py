from sentry_sdk import capture_exception


def parseQuery(path):
    """
    Parses the query string from the URL path and returns a dictionary of key-value pairs.
    Returns:
        dict: A dictionary containing the parsed query parameters.
    Raises:
        Exception: If an error occurs during parsing.
    """
    # code implementation
    try:
        queryDict = {}

        if "?" not in path:
            return queryDict

        pathParts = path.split("?")

        if len(pathParts) == 0:
            return queryDict

        query = pathParts[1]
        queryParts = query.split("&")

        if len(queryParts) == 0:
            return queryDict

        for part in queryParts:
            key, value = part.split("=")
            queryDict[key] = value
        return queryDict
    except Exception as e:
        capture_exception(e)
