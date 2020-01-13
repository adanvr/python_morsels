

def ini2csv(filename):
    open_file = open(filename)
    with open_file:
        file_contents = open_file.read()
        print(file_contents)