import json
from typing import List, Tuple

import emoji

from src.modules.constants import COUNTER_INDEX, TOP_N


def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """Recover top 10 most mentioned users and the count of the mentions.
    
    Parameters:
    file_path (srt): a path where is located the file we want to read

    Returns:
    list: a sorted list with a tuple with the emoji and the counter of usage
    """
    emoji_counter = {}

    with open(file_path, 'r', encoding='utf-8', buffering=1) as json_file:
        for line in json_file:
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

    # ToDo: Check if is possible to avoid sort at the end and keep top_n sorted
    sorted_emojies = {
        emoji: counter for emoji, counter in sorted(
            emoji_counter.items(), key=lambda item: item[COUNTER_INDEX],
            reverse=True
        )
    }

    # Format in the desired output
    top_n_emojies = [
        (emoji, sorted_emojies[emoji]) for emoji in list(sorted_emojies)[:TOP_N]
    ]

    return top_n_emojies
