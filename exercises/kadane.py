# Implementing Kardne's alogrithm using dynamic programming
def kadaned(lst):
    if not len(lst):
        return "List is empty"
    maxsum = cursum = lst[0]
    for i in lst[1:]:
        cursum = max(i, cursum+i)
        maxsum = max(maxsum, cursum)
    return maxsum

def kadane(lst):
    if not len(lst):
        return "List is empty"
    maxsum = cursum = lst[0]
    for i in lst[1:]:
        cursum = cursum + i if cursum + i > i else i
        maxsum = cursum if cursum > maxsum else maxsum
    return maxsum

print kadaned([-3,-1,-4,-6,-3])
