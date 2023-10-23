from typing import List, Tuple
from datetime import datetime
import os

from src.modules.constants import PIPELINE_ARGS
from src.pipelines.q1_time import run


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    run(file_path, PIPELINE_ARGS)

    files_paths = [x for x in os.listdir('./results/q1/')]
    file_path = os.path.join('./results/q1/' , files_paths[0])

    # This is a nonsense, just to return the value as desired
    with open(file_path, 'r', encoding='utf-8', buffering=1) as file:
        import datetime

        for line in file:
            result = eval(line)

    return result
