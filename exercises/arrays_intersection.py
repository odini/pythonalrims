def find_intersection(seq1, seq2):
    intersection = set()
    i, j = 0, 0
    while (i < len(seq1) and j < len(seq2)):
        if seq1[i] == seq2[j]:
            intersection.add(seq1[i])
            i += 1
        elif seq1[i] < seq2[j]:
            i += 1
        elif seq1[i] > seq2[j]:
            j += 1
    return intersection

l1 = [1, 3, 5, 6, 9, 10]
l2 = [1, 4, 6, 8, 10]
print find_intersection(l1,l2)
