import json

def parse_element(element: str) -> str:
    """Read a json like string and return 'renderedContent' value."""
    element = json.loads(element)
    return element['renderedContent']
