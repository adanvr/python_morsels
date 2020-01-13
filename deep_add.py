from typing import List

def flatten(l : list) -> list:
    for item in l:
        if hasattr(item, "__iter__") and not isinstance(item, str):
            for x in flatten(item):
                yield x
        else:
            yield item

def deep_add(L : list, start = 0) -> int:
    ''' Function takes a nested list of int and sums them up '''
    flattened = list(flatten(L))
    if flattened == []:
        return 0 + start
    else:
        return sum(flattened) + start
    

assert deep_add([1, 2, 3, 4]) == 10
assert deep_add([[1, 2, 3], [4, 5, 6]]) == 21
assert deep_add([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) == 36
assert deep_add([[], []]) == 0
assert deep_add([[1, 2], [3, 4]], start=2) == 12
assert deep_add([(1, 2), [3, {4, 5}]]) == 15