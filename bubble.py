# Bubble Sort compares only two items at a time, then confirms by comparing
# them one by one again.  Takes as long as it takes.  Is O(n^2) complexity

import unittest
import itertools

def bubble(in_string):

    lo = []
    for i in in_string:
        lo.append(int(i))
    j = 0

    while j < len(lo):
        if lo[j] > lo[j+1]:
            smaller = lo[j+1]
            bigger = lo[j]
            lo[j] = smaller
            lo[j+1] = bigger # need to conditional this one out
        j += 1
        print lo

#        if j == lo[-1]: # this is a check to see if we're at the end of the list
#            return lo
#        if lo[j] <= lo[j+1]:
#            pass
#        elif lo[j] > lo[j+1]:
#            lo[j+1] = lo[j]

bubble('63782541')

# do tests outside this file to test speed
