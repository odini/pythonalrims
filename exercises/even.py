def even_sum(li,n=1):
    j = [None]*n
    while n != 0:
        for i in li:
            if i % 2 == 0 and i > j[n-1]:
                j[n-1] = i
        li.remove(j[n-1])
        n -=1
    return sum(j)

li = [-2,-5,2,5,4,18,9,13,22,33]
print even_sum(li,4)
