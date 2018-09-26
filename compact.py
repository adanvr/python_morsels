from itertools import groupby

def compact_iter(iterable):
    return (item for item, in groupby(iterable))

# The groupby function groups consecutive items in an iterable that are equivalent (the behavior can be customized slightly if a key function is specified, but we're not doing that). 
# We're squashing consecutive duplicate items into just 1, so the keys coming back from the groupby function are all we really need to make our new iterable.

def compact(iterable):
    '''
    Return new iterable with adjacent duplicate values removed.
    '''
    previous = object()
    for item in iterable:
        if item != previous:
            yield item
            previous = item


# We're using a generator function here. Generator functions are unlike regular functions. 
# They return a generator object which will return items every time a yield statement is hit in our generator function.




def compact_og(sequence):
    '''
    write a function that accepts a sequence (a list for example) and returns a new iterable (anything you can loop over) with adjacent duplicate values removed.
    '''
    deduped = []
    for i, item in enumerate(sequence):
        if i == 0 or item != sequence[i-1]:
            deduped.append(item)
    return deduped
    


def compact_zipped(sequence):
    '''
    Another way you could solve this is to zip together the original sequence with itself shifted by one so that the each item can compare itself with the one before.
    The * here is "unpacking" each of the items in our sequence into this new list, after object(). We're making object() the first item in our second list because a new
    object will not be compared as equal to any of the items in sequence (each object is only equal to itself by default).
    '''
    deduped = []
    for item, previous in zip(sequence, [object(), *sequence]):
        if item != previous:
            deduped.append(item)
    return deduped
    