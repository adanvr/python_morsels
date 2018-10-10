from collections import deque

def tail(iterable, n):
    """Return the last n items of given iterable."""
    if n <= 0:
        return []
    return list(deque(iterable, maxlen=n))