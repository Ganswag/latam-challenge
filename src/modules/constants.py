"""Some constants we use, sorted alphabetically"""

from datetime import datetime

COUNTER_INDEX = 1
DATE_INDEX = 0
DUMMY_DATE = datetime.fromisoformat('2050-01-01T00:00:00+00:00').date()
FILE_PATH = './farmers-protest-tweets-2021-2-4.json'
READ_MODE = 'r'  # Reading mode to open files
TOP_N = 10  # First Top N elements we want
TOP_USERNAME_INDEX = 2
PIPELINE_ARGS = {'flexrs_goal': 'SPEED_OPTIMIZED'}
USERNAME_INDEX = 0
