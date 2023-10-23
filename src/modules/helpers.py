
def insert_sorted(iterable: list, element: tuple, el_idx: int) -> list:
    """Add the 'element' into 'iterable' comparing the index 'el_index' in
    a DESC way.

    WARNING: Keep in mind this only will work for positive numbers because
    counters cannot be negative.

    Parameters:
    iterable (list): sorted array where we want to add the new 'entry'
    element (tuple): the new element we want to add to 'iterable'
    el_indx (int): index to compares
    """
    i = 0
    element[el_idx]  # check if element index exists or raise error if not

    if not iterable or element[el_idx] < iterable[-1][el_idx]:
        iterable.append(element)
    else:
        while element[el_idx] < iterable[i][el_idx] and i < len(iterable):
            i += 1
        iterable.insert(i, element)


def get_max_value(counter_by_key: dict) -> tuple:
    """Returns a tuple (key, value) for the maximum value in a dictionay

    WARNING: Keep in mind this only will work for positive numbers because
    counters cannot be negative.
    """
    COUNTER_INDEX = 1

    max_value = ('__initial__', -1)  # Initialize a dummy data
    for key, counter in counter_by_key.items():
        # The following line implies we'll get the first founded max
        if counter > max_value[COUNTER_INDEX]:
            max_value = (key, counter)

    return max_value
