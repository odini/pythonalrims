#Iterative and recursive implementation for finding n max elements in a list
def listmaxn(lst,n):
    res = []
    while n != 0:
        curmax = lst[0]
        for i in lst[1:]:
            curmax = i if i > curmax else curmax
        lst.remove(curmax)
        res.append(curmax)
        n -= 1
    return res

def reclistmaxn(lst,n):
    if not (lst and n):
        return []
    curmax = lst[0]
    for i in lst[1:]:
        curmax = i if i > curmax else curmax
    lst.remove(curmax)
    return [curmax] + reclistmaxn(lst,n-1)

print reclistmaxn([-15,10,20,15,1,4,5,15,3],3)
