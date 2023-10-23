from datetime import datetime
import json
from typing import List, Tuple

from src.modules.constants import DUMMY_DATE, TOP_N
from src.modules.helpers import get_max_value, insert_sorted


def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    tweets_counter_by_user = {}
    max_user_by_date = []
    tweets_by_day = 0
    prev_date = DUMMY_DATE

    with open(file_path, 'r', encoding='utf-8', buffering=1) as json_file:
        for line in json_file:
            tweets_by_day += 1
            _line = json.loads(line)

            date = datetime.fromisoformat(_line['date']).date()
            user = _line['user']['username']

            if prev_date != date:  # this is because date is always descendent
                max_value = get_max_value(tweets_counter_by_user)

                insert_sorted(
                    max_user_by_date,
                    (prev_date, tweets_by_day - 1, max_value[0]),
                    1
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
            (prev_date, tweets_by_day - 1, max_value[0]),
            1
        )
        if len(max_user_by_date) > TOP_N:  # We only want TOP_N results
            max_user_by_date.pop()

    return [(el[0], el[2]) for el in max_user_by_date]
