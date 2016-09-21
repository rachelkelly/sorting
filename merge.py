# Skeleton file for Merge Sort, a type of sorting which separates
# items into one, then sorts and compares them by twos, then sorts
# and compares them by fours, then sorts and compares them by eights, 
# and so forth.  Is complexity O(n n).  O(log n)?

def merge(in_string):
    lo = []
    for i in in_string:
        lo.append(int(i))

    # now to collect them in groups of 2, putting the lower number first
