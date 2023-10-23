from typing import List, Tuple
import os

from src.modules.constants import PIPELINE_ARGS
from src.pipelines.q2_time import run


def q2_time(file_path: str) -> List[Tuple[str, int]]:
    """Recover top 10 most mentioned users and the count of the mentions.
    
    Parameters:
    file_path (srt): a path where is located the file we want to read

    Returns:
    list: a sorted list with a tuple with the username and the
    counter of mentions
    """
    run(file_path, PIPELINE_ARGS)

    # This is a nonsense, just to read the file from the pipeline 
    # and return the value as desired because pipelines returns nothing
    files_paths = [x for x in os.listdir('./results/q2/')]
    file_path = os.path.join('./results/q2/' , files_paths[0])

    with open(file_path, 'r', encoding='utf-8', buffering=1) as file:
        import datetime

        for line in file:
            result = eval(line)

    return result
