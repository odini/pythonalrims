#Iterative and recursive implementation for finding n max elements in a list
def listmaxn(l,n):
    max = []
    while n != 0:
        currmax = l[0]
        for i in l:
            if i >= currmax:
                currmax = i
        l.remove(currmax)
        max.append(currmax)
        n -= 1
    return max

def reclistmaxn(l,n):
    if n == 0:
        return []
    currmax = l[0]
    for i in l:
        if i >= currmax:
            currmax = i
    l.remove(currmax)
    return [currmax] + reclistmaxn(l,n-1)

print listmaxn([-15,10,20,15,1,4,5,15,3],3)
