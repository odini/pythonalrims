# Implementing Kardne's alogrithm using dynamic programming
def kadane(seq):
    if not len(seq):
        return "List is empty"
    max_sum, cur_sum = seq[0], seq[0]
    s_index, e_index = 0, 0
    for index, item in enumerate(seq[1:]):
        cur_sum = max(item, cur_sum + item)
        max_sum = max(max_sum, cur_sum)
    return max_sum

def kadaned(seq):
    if not len(seq):
        return "List is empty"
    max_sum, cur_sum = seq[0], seq[0]
    for item in seq[1:]:
        if (cur_sum + item) > item:
            cur_sum += item
        else:
            cur_sum = item
        if cur_sum > max_sum:
            max_sum = cur_sum
    return max_sum

print kadaned([-3,-1,-4,-6,-3])
