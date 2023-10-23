from typing import List, Tuple
from datetime import datetime
import os

from src.modules.constants import PIPELINE_ARGS
from src.pipelines.q1_time import run


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    """Recover most active user for by the date with most tweets from a file
    sorted in a descendent way based on the the tweets by date.
    
    Parameters:
    file_path (srt): a path where is located the file we want to read

    Returns:
    list: a sorted list with a tuple with date and the username with most
        tweets in the date  
    """
    run(file_path, PIPELINE_ARGS)

    # This is a nonsense, just to read the file from the pipeline 
    # and return the value as desired because pipelines returns nothing
    files_paths = [x for x in os.listdir('./results/q1/')]
    file_path = os.path.join('./results/q1/' , files_paths[0])

    with open(file_path, 'r', encoding='utf-8', buffering=1) as file:
        import datetime

        for line in file:
            result = eval(line)

    return result
