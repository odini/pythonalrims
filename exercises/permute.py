# Implementing string permutation algorithm

def permute(s):
    if len(s) == 1:
        return s
    res = []
    for i in xrange(len(s)):
        perm = s[:i] + s[i+1:]
        z = permute(perm)
        for t in z:
            res.append(s[i]+t)

    return res

print permute('abc')
