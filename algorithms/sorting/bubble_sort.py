def bubble_sort(seq):
    L = len(seq) - 1
    for i in xrange(L, 0, -1):
        for j in xrange(L):
            if seq[j+1] < seq[j]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq

alist = [-54,26,93,17,77,31,11,17,44,55,20,100,32,14]
print bubble_sort(alist)
