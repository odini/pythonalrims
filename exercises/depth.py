def depth(data,n=1):
    result = []
    for l in data:
        if l is list:
            result.append(l)
        if l is list:
            return depth(l)
        print l

depth([1, 2, [3, 4, [5, 6]], [7]])
