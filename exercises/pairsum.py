from timedecorator import *

@timedecorator
def pair_sum(seq,k):
    if len(seq) < 2:
        return "List has less than a pair of elements"
    seq.sort()
    L, R = 0, len(seq)-1
    while L < R:
        if (seq[L] + seq[R]) == k:
            print (seq[L], seq[R])
            L += 1
        elif (seq[L] + seq[R]) < k:
            L += 1
        else:
            R -= 1

# Implement using dict
def pair_sumd(seq,k):
    match = {}
    for index in range(len(seq)):
        if seq[index] not in match.keys():
            match[seq[index]] = [index]
        else:
            match[seq[index]].append(index)
        if (k - seq[index]) in match.keys():
            print seq[index], k-seq[index]

    return match

# l = random.sample(xrange(100*100),50*50)
l = [1,1,2,4,6,8,9,9,10]
print pair_sumd(l,10)
