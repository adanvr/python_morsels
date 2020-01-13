from collections import defaultdict
def group_by(iterable, key_func = lambda x: x):
    '''
    This function takes an iterable and a key function and returns a dictionary of items grouped by the values returned by the given key function.
    '''
    #This defaultdict object is kind of cool. Whenever a missing key is accessed, 
    # defaultdict will call the callable that was given to it (list in this case) and use the return value as the new value for that key.
    groups = defaultdict(list)
    for item in iterable:
        groups[key_func(item)].append(item)
    return groups
