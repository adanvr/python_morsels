import csv

def csv_columns(file):
    '''
    This function accepts a file object and returns a dictionary mapping CSV headers to column data for each header.
    Example:
    h1,h2
    1,2
    3,4
    Returns:
    {'h1': ['1', '3'], 'h2': ['2', '4']}
    '''
    with open(file) as f:
        data = [row for row in csv.reader(f)]
    tmp = {}
    lst = []
    vals = []
    for i in range(len(data[1:])):
        vals = [item[i]  for item in data[1:]]
        lst.append(vals) 
    for i in range(len(lst)):
        tmp[i] = lst[i]
        tmp[data[0][i]] = tmp.pop(i)
    return tmp

data = csv_columns('my_file.csv')


