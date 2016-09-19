# Bubble Sort compares only two items at a time, then confirms by comparing
# them one by one again.  Takes as long as it takes.  Is O(n^2) complexity

import unittest

def bubble(in_string):

    lo = []
    for i in in_string:
        lo.append(int(i))
    i = 0 # using i again as index convention

    while i < len(lo):
        if lo[i+1] == len(lo):
            break
        if lo[i] > lo[i+1]:
            smaller = lo[i+1]
            bigger = lo[i]
            lo[i] = smaller
            lo[i+1] = bigger
        print lo
        i += 1

bubble('63752841')

# do tests outside this file to test speed
