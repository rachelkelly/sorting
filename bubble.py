# Bubble Sort compares only two items at a time, then confirms by comparing
# them one by one again.  Is O(n^2) complexity

def bubble(in_string):

    lo = []
    for i in in_string:
        lo.append(int(i))
    goodness = 0 # if comparison doesn't need to be made, ticks up
    pass_count = 0 # counts number of full loops needed

    while goodness < len(lo):
        i = 0
        goodness = 0 
        while i < len(lo):
            if i+1 == len(lo):
                break
            if lo[i] <= lo[i+1]:
                goodness += 1
                if goodness == (len(lo)-1):
                    print "input string: %s" %in_string
                    print "sorted output: %s" % lo
                    print "how many passes it took: %d " % pass_count
                    return lo
            elif lo[i] > lo[i+1]:
                smaller = lo[i+1]
                bigger = lo[i]
                lo[i] = smaller
                lo[i+1] = bigger
            i += 1
            pass_count += 1

