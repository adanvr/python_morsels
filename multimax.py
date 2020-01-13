def multimax(iterable, key = lambda x: x):
    '''
    This function takes an iterable and returns all the maximum values found in that iterable.
    Also should accept a key argument which is a function that will determine how our values should be compared to each other - almost like a "score".
    '''
    max_key = None
    maximums = []
    #We could score a list of items and their scores, find the max score and then return all items with that score.
    for item in iterable:
        k = key(item)
        if k == max_key:
            maximums.append(item)
        elif not maximums or k > max_key:
            maximums = [item]
            max_key = k
    return maximums