def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist)/2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)

        k = 0
        while len(lefthalf) and len(righthalf):
            if lefthalf[0] < righthalf[0]:
                alist[k] = lefthalf.pop(0)
            else:
                alist[k] = righthalf.pop(0)
            k += 1

        alist[k:k+len(lefthalf)] = lefthalf
        alist[k:k+len(righthalf)] = righthalf

alist = [54,26,93,17,77,31,11,17,44,55,20,100,32,14]
merge_sort(alist)
print alist
