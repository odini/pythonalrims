def reverse(test):
    if not len(test):
        return test
    return reverse(test[1:]) + [test[0]]

print reverse([1,2,3])
