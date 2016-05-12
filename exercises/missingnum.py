# Implementing using sorting and binary search. Complexity O(nlogn)
def findMissing1(lst1,lst2):
    lst1.sort()
    lst2.sort()
    for i,j in zip(lst1,lst2):
        if i != j:
            return i

# Implementing using XORing trick. Complexity is O(n)
def findMissing2(lst1,lst2):
    result = 0
    print lst1+lst2
    for i in lst1+lst2:
        print result
        result ^= i
    return result

l1 = [1,4,4,5,7,8]
l2 = [1,4,5,7,8]
print findMissing1(l1,l2)
