def push_zeros(seq):
    L, R = 0, len(seq) - 1
    while ( L <= R and R > 0 ):
        while ( seq[R] == 0 and R > L):
            R -= 1
        if seq[L] == 0:
            seq[L], seq[R] = seq[R], seq[L]
            R -= 1
        L += 1
    return seq

alist = [0, 0, 0, 0]
print push_zeros(alist)
