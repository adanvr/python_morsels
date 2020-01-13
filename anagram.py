import unicodedata
from collections import Counter

def remove_accents(string):
    """Return decomposed form of the given string."""
    return unicodedata.normalize('NFKD', string)

def count_letters(string):
    """Return sorted list of letters in given string."""
    return Counter(
        char
        for char in string.lower()
        if char.isalpha()
    )

def is_anagram(word1, word2):
    """Return True if the given words are anagrams."""
    return count_letters(word1) == count_letters(word2)
