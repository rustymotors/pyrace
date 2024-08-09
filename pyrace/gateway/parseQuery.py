from sentry_sdk import capture_exception
from urllib.parse import urlparse, parse_qs


def parseQuery(path):
    try:
        queryDict = parse_qs(urlparse(path).query)
        return {k: v[0] for k, v in queryDict.items()}
    except Exception as e:
        capture_exception(e)
        return {}
