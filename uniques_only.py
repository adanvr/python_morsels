def uniques_only(iterable):
    '''
    This function accepts an iterable and returns a new iterable with all items from the original iterable except for duplicates
    '''
    uniques = []
    for i in iterable:
        if i not in uniques:
            uniques.append(i)            
    return (n for n in uniques)

    
