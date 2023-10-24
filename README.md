# Data Engineer Challenge
​
## Welcome

This is a solution to LATAM challenge, this was developed using python=3.9.6
​
## Challenge
In this [file](https://drive.google.com/file/d/1ig2ngoXFTxP5Pa8muXo02mDTFexZzsis/view?usp=sharing) you will find a 398MBs dataset. There are **2 approaches for each problem**: The first one optimizing execution time, and the 
other one optimizing usage memory.

The solutions are in 6 files in the `src` path. 
Each file has a function with the same name with tthe specified format bellow.
Also in the `.ipynb` file is detailed the process thinking.
​
1. Top 10 dates with most tweets. And the username with most publications in that
day.
```python
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
```
```python
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
```
```python
Returns: 
[(datetime.date(1999, 11, 15), "LATAM321"), (datetime.date(1999, 7, 15), "LATAM_CHI"), ...]
```
​
2. Top 10 emojis and their respective counter.
```python
def q2_time(file_path: str) -> List[Tuple[str, int]]:
```
```python
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
```
```python
Returns: 
[("✈️", 6856), ("❤️", 5876), ...]
```
3. Top 10 mentioned usernames and ther mentions counter.
```python
def q3_time(file_path: str) -> List[Tuple[str, int]]:
```
```python
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
```
```python
Returns: 
[("LATAM321", 387), ("LATAM_CHI", 129), ...]
```

## Sugestions
* To measure the usage memory we recomend [memory-profiler](https://pypi.org/project/memory-profiler/) or [memray](https://github.com/bloomberg/memray)
* To measure execution time we recomend [py-spy](https://github.com/benfred/py-spy) or [Python Profilers](https://docs.python.org/3/library/profile.html)​

## Run tests
Some basic tests were implemented, in order to execute it just run:

```bash
python3 tests
```

## ToDo
* Add sample data and create functional tests
* Use memory profiler as sugested in the README.md
