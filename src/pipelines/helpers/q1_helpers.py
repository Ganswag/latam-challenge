import json
from datetime import datetime


def parse_element(element):
    element = json.loads(element)
    return (
        str(datetime.fromisoformat(element['date']).date()),
        element['user']['username']
    )


def format_output(element):
   return [
        (
           datetime.strptime(el[0], '%Y-%m-%d').date(),
           el[1][1]
        ) for el in element
    ]
