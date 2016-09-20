# Bubble Sort compares only two items at a time, then confirms by comparing
# them one by one again.  Takes as long as it takes.  Is O(n^2) complexity

import unittest

def bubble(in_string):

    lo = []
    for i in in_string:
        lo.append(int(i))
    goodness = 0 # if comparison doesn't need to be made, ticks up
    badness_counter = 0 # counts number of full loops needed

    while goodness < len(lo):
        i = 0
        #goodness_counter = 0 # haha crap, putting it here makes it asplode
        while i < len(lo):
            goodness = 0 # to reset it every time
            if i+1 == len(lo):
                break
            if lo[i] <= lo[i+1]:
                goodness += 1
                if goodness == len(lo):
                    print "inner lo: %d" %lo
                    #p = 1
                    return True # may not need to reset val of p
            elif lo[i] > lo[i+1]:
                smaller = lo[i+1]
                bigger = lo[i]
                lo[i] = smaller
                lo[i+1] = bigger
            i += 1
            badness_counter += 1
            print "outer lo and # of loops" 
            print lo, badness_counter

bubble('63752841')

# do tests outside this file to test speed
