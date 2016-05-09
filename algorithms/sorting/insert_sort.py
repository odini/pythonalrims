def insert_sort(alist):
    for index in range(1,len(alist)):
        counter = index
        while ((counter>0) and (alist[counter]<alist[counter-1])):
            temp = alist[counter-1]
            alist[counter-1] = alist[counter]
            alist[counter] = temp
            counter -= 1

alist = [54,26,93,17,77,31,11,17,44,55,20,100,32,14]
insert_sort(alist)
print alist
