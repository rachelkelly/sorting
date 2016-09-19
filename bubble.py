# Bubble Sort compares only two items at a time, then confirms by comparing
# them one by one again.  Takes as long as it takes.  Is O(n^2) complexity

import unittest
import itertools

def bubble(in_string):

    for i in in_string:
        lo.append(int(i))
    j = 0
    while j < len(lo):
        k = lo[j+1]
        if k == lo[-1]: 
            if lo[j] > lo[k]: # or should this be `if lo[j] > k`
                intermed = lo[k] # set smaller value at EOL to intermed
                lo[k] = lo[j] # move value at lo[j] to EOL bc is bigger
                lo[j] = intermed # set lower value in list to smaller value
            break
        if lo[j] > lo[j+1]:
            intermediary = lo[j+1]
        j += 1

    print "unsorted %s" % lo
    for j in lo:
        print j
        if j == lo[-1]: # this is a check to see if we're at the end of the list
            return lo
        if lo[j] <= lo[j+1]:
            pass
        elif lo[j] > lo[j+1]:
            lo[j+1] = lo[j]

bubble('63782541')

# do tests outside this file to test speed
