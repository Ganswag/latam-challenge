import json
import re
from typing import List, Tuple

from src.modules.constants import COUNTER_INDEX, TOP_N


def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """Recover top 10 most mentioned users and the count of the mentions.
    
    Parameters:
    file_path (srt): a path where is located the file we want to read

    Returns:
    list: a sorted list with a tuple with the username and the
    counter of mentions
    """
    mentions_counter = {}

    with open(file_path, 'r', encoding='utf-8', buffering=1) as json_file:
        for line in json_file:
            _line = json.loads(line)
            tweet_content = _line['renderedContent']
            mentioned_users = re.findall(r'@(\w+)\b', tweet_content)

            for user in mentioned_users:
                if mentions_counter.get(user):
                    mentions_counter[user] += 1
                else:
                    mentions_counter[user] = 1

    # ToDo: Check if is possible to avoid sort at the end and keep top_n sorted
    all_mentions_sorted = {
        username: mentions_counter for username, mentions_counter in
        sorted(
            mentions_counter.items(), key=lambda item: item[COUNTER_INDEX],
            reverse=True
        )
    }
    top_n_mentions = [
        (username, all_mentions_sorted[username])
        for username in list(all_mentions_sorted)[:TOP_N]
    ]

    return top_n_mentions
