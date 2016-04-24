def reverse(test):
    if not len(test):
        return test
    return reverse(test[1:]) + [test[0]]

def rec_reverse(test):
    result = []
    for i in xrange(len(test),0,-1):
        result.append(test[i-1])
    return result

print rec_reverse([1,2,3])
