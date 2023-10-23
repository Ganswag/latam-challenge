import json

def parse_element(element):
    element = json.loads(element)
    return element['renderedContent']
