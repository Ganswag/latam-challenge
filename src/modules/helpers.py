
def insert_sorted(iterable: list, element: tuple, el_idx: int) -> list:
    i = 0
    element[el_idx]  # check if element index exists or raise error if not

    if not iterable or element[el_idx] < iterable[-1][el_idx]:
        iterable.append(element)
    else:
        while element[el_idx] < iterable[i][el_idx] and i < len(iterable):
            i += 1
        iterable.insert(i, element)


def get_max_value(tweets_counter_by_user: dict) -> tuple:
    """ Returns a tuple (key, value) for the maximum value in a dictionay

    WARNING: Keep in mind this only will work for positive numbers because
    tweet counter cannot be negative.
    """
    max_value = ('__initial__', -1)  # Initialize a dummy data
    for user_name, tweets_counter in tweets_counter_by_user.items():
        # The following line implies we'll get the first founded max
        if tweets_counter > max_value[1]:
            max_value = (user_name, tweets_counter)

    return max_value