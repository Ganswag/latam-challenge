import json
from typing import List, Tuple

import emoji

from src.modules.constants import TOP_N


def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    emoji_counter = {}

    with open(file_path, 'r', encoding='utf-8', buffering=1) as json_file:
        for line in json_file:
            tweets_by_day += 1
            _line = json.loads(line)
            tweet_content = _line['renderedContent']

            # This is trully slow, but since Indi characters are used I couldn't 
            # find a better solution far now :(
            # I'd like to use a regex to find just emojies
            used_emojis = [el['emoji'] for el in emoji.emoji_list(tweet_content)]

            for _emoji in used_emojis:
                if emoji_counter.get(_emoji):
                    emoji_counter[_emoji] += 1
                else:
                    emoji_counter[_emoji] = 1

    sorted_emojies = {
        k: v for k, v in sorted(
            emoji_counter.items(), key=lambda item: item[1], reverse=True
        )
    }
    top_n_emojies = [
        (k, sorted_emojies[k]) for k in list(sorted_emojies)[:TOP_N]
    ]

    return top_n_emojies
