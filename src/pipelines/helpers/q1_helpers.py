import json
from datetime import datetime
from typing import List, Tuple


def parse_element(element:str) -> Tuple[str, str]:
    """Read an json valid string and return as tuple with the
    formated date and the username

    Parameters:
    element (srt): a string with a valid json

    Returns:
    tuple: a date in index 0, the username in the index 1
    """
    element = json.loads(element)
    return (
        str(datetime.fromisoformat(element['date']).date()),
        element['user']['username']
    )


def format_output(elements: list) -> List[Tuple[datetime.date, int]]:
    """Just format the date and get the username

    Parameters:
    elements (list): a list with tuples inside with (date, (counter, username))

    Returns:
    tuple: a date in index 0, the username in the index 1
    """
    DATE_INDEX = 0
    USERNAME_INDEX, MOST_ACTIVE_USER_INDEX = 1

    return [
        (
           datetime.strptime(el[DATE_INDEX], '%Y-%m-%d').date(),
           el[MOST_ACTIVE_USER_INDEX][USERNAME_INDEX]
        ) for el in elements
    ]
