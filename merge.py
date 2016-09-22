# Skeleton file for Merge Sort, a type of sorting which separates
# items into one, then sorts and compares them by twos, then sorts
# and compares them by fours, then sorts and compares them by eights, 
# and so forth.  Is complexity O(n n).  O(log n)?

def merge(in_string):
    lo = []
    for i in in_string:
        lo.append(int(i))

    # now to collect them in groups of 2, putting the lower number first
    i = 0
    twos = []
    new = []
    while i < len(lo):
        while len(new) < 2:
            new.append(lo[i])
            i += 1 
        twos.append(new)
        new = []
        # i += 1
    print twos

merge('36728541')
