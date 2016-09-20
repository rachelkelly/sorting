# Bubble Sort compares only two items at a time, then confirms by comparing
# them one by one again.  Takes as long as it takes.  Is O(n^2) complexity

import unittest

def bubble(in_string):

    lo = []
    for i in in_string:
        lo.append(int(i))
    goodness_counter = 0
    p = 0 # part of a bad solution haha

    while p == 0: # haha whoa
        i = 0
        #goodness_counter = 0 # haha crap, putting it here makes it asplode
        while i < len(lo):
            if lo[i+1] == len(lo):
                break
            if lo[i] <= lo[i+1]:
                goodness_counter += 1
                if goodness_counter == len(lo):
                    print lo
                    #p = 1
                    return True
            elif lo[i] > lo[i+1]:
                smaller = lo[i+1]
                bigger = lo[i]
                lo[i] = smaller
                lo[i+1] = bigger
            print lo
            i += 1

bubble('63752841')

# do tests outside this file to test speed
