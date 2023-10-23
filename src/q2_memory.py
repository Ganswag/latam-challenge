import json
import re
from typing import List, Tuple

from src.modules.constants import TOP_N


def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    mentions_counter = {}

    with open(file_path, 'r', encoding='utf-8', buffering=1) as json_file:
        for line in json_file:
            tweets_by_day += 1
            _line = json.loads(line)
            tweet_content = _line['renderedContent']
            mentioned_users = re.findall(r'@(\w+)\b', tweet_content)

            for user in mentioned_users:
                if mentions_counter.get(user):
                    mentions_counter[user] += 1
                else:
                    mentions_counter[user] = 1

    all_mentions_sorted = {
        k: v for k, v in 
        sorted(mentions_counter.items(), key=lambda item: item[1], reverse=True)
    }
    top_n_mentions = [
        (k, all_mentions_sorted[k]) for k in list(all_mentions_sorted)[:TOP_N]
    ]

    return top_n_mentions
