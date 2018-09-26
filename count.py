#>>> count_words("oh what a day what a lovely day")
#{'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
#>>> count_words("don't stop believing")
#{"don't": 1, 'stop': 1, 'believing': 1}
import collections 
from collections import Counter
from collections import defaultdict
import regex as re

def count_words_adan(word_str):
    '''
    Function that will create a dictionary of count of words in string 
    '''
    new_dict_for = {}
    for word in word_str.split():
        if word not in new_dict_for:
            new_dict_for[word] = 1
        new_dict_for[word] += 1
    return new_dict_for


def count_words_2(string):
    """Return the number of times each word occurs in the string."""
    count = defaultdict(int)
    for word in string.split():
        count[word] += 1
    return count

def count_words(string):
    """Return the number of times each word occurs in the string."""
    return Counter(re.findall(r"[\w'-]+", string.lower()))