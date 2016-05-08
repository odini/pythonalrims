#! /usr/bin/python
from collections import defaultdict
# This function will use count and compare method to check if two strings are anagrams

def anagramSolver(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] += 1

    j = 0
    match = True

    while j<26 and match:
        if c1[j] == c2[j]:
            j += 1
        else:
            match = False
    print c1,c2
    return match

# Using dictionaries
def anagrams(s1,s2):
    if len(s1) != len(s2):
        return False
    ang = defaultdict(int)
    for i in s1.lower():
        ang[i] += 1

    for i in s2.lower():
        ang[i] -= 1
        if ang[i] < 0:
            return False
    return True

print anagrams('Odia','odin')
