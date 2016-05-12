from timedecorator import *

@timedecorator
def pairsum(lst,k):
    if len(lst) < 2:
        return "List has less than a pair of elements"
    lst.sort()
    L, R = 0, len(lst)-1
    while L < R:
        if (lst[L]+lst[R]) == k:
            print (lst[L],lst[R])
            L += 1
        elif (lst[L]+lst[R]) < k:
            L += 1
        else:
            R -= 1

# Implement using dict
def pairsumd(lst,k):
    match = {}
    for i in range(len(lst)):
        if not lst[i] in match.keys():
            match[lst[i]] = [i]
        else:
            match[lst[i]].append(i)
        if k - lst[i] in match.keys():
            print lst[i],k-lst[i]

    return match

# l = random.sample(xrange(100*100),50*50)
l = [1,1,2,4,6,8,9,9,10]
print pairsumd(l,10)
