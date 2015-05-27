#!/usr/bin/python
def insertsort(s):
    for index in range(1,len(s)):
        counter = index
        while ((counter>0) and (s[counter]<s[counter-1])):
            temp = s[counter-1]
            s[counter-1] = s[counter]
            s[counter] = temp
            counter -= 1
    return s
