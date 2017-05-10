""" Counts the occurrances of words or characters in a sentence"""

from collections import Counter



def Word_count(line):

    line = line.split()

    word_count = {}

    for word in line:

        word_count[word] = line.count(word)

    return '\n'.join("{}: {}".format(k, v) for k, v in word_count.items())




print(Word_count("my oh my ! What a wonderful day ! !"))