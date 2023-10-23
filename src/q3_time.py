from typing import List, Tuple
import os

from src.modules.constants import PIPELINE_ARGS
from src.pipelines.q3_time import run


def q3_time(file_path: str) -> List[Tuple[str, int]]:
    run(file_path, PIPELINE_ARGS)

    files_paths = [x for x in os.listdir('./results/q3/')]
    file_path = os.path.join('./results/q3/' , files_paths[0])

    # This is a nonsense, just to return the value as desired
    with open(file_path, 'r', encoding='utf-8', buffering=1) as file:
        import datetime

        for line in file:
            result = eval(line)

    return result
