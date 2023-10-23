from datetime import datetime
import json
from typing import List, Tuple

from src.modules.constants import (
    COUNTER_INDEX, DATE_INDEX, DUMMY_DATE,
    TOP_N, TOP_USERNAME_INDEX, USERNAME_INDEX
)
from src.modules.helpers import get_max_value, insert_sorted



def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    """Recover most active user for by the date with most tweets from a file
    sorted in a descendent way based on the the tweets by date.
    
    Parameters:
    file_path (srt): a path where is located the file we want to read

    Returns:
    list: a sorted list with a tuple with date and the username with most
        tweets in the date  
    """
    max_user_by_date = []
    tweets_by_day = 0
    tweets_counter_by_user = {}
    prev_date = DUMMY_DATE

    with open(file_path, 'r', encoding='utf-8', buffering=1) as json_file:
        for line in json_file:
            tweets_by_day += 1
            _line = json.loads(line)

            date = datetime.fromisoformat(_line['date']).date()
            user = _line['user']['username']

            # this is because date is always descendent:
            if prev_date != date and prev_date != DUMMY_DATE:
                max_value = get_max_value(tweets_counter_by_user)

                insert_sorted(
                    max_user_by_date,
                    (prev_date, tweets_by_day - 1, max_value[USERNAME_INDEX]),
                    COUNTER_INDEX
                )
                if len(max_user_by_date) > TOP_N:  # We only want TOP_N results
                    max_user_by_date.pop()

                tweets_counter_by_user = {}
                tweets_by_day = 1

            prev_date = date

            if tweets_counter_by_user.get(user):
                tweets_counter_by_user[user] += 1
            else:
                tweets_counter_by_user[user] = 1

        # Compute data for last date:
        max_value = get_max_value(tweets_counter_by_user)
        insert_sorted(
            max_user_by_date,
            (prev_date, tweets_by_day - 1, max_value[USERNAME_INDEX]),
            COUNTER_INDEX
        )
        if len(max_user_by_date) > TOP_N:  # We only want TOP_N results
            max_user_by_date.pop()

    return [(el[DATE_INDEX], el[TOP_USERNAME_INDEX]) for el in max_user_by_date]
