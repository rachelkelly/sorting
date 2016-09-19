# Bubble Sort compares only two items at a time, then looks at the entirety
# and then compares them one by one again.

import unittest
import itertools

def bubble(in_string):


    while i < len(lo):
        itertools.cycle(lo)
        i += 1

    listy = []
    for i in in_string:
        listy.append(int(i))
    print "unsorted %s" % listy
    for j in listy:
        print j
        if j == listy[-1]: # this is a check to see if we're at the end of the list
            return listy
        if listy[j] <= listy[j+1]:
            pass
        elif listy[j] > listy[j+1]:
            listy[j+1] = listy[j]

bubble('63782541')

# do tests outside this file to test speed
