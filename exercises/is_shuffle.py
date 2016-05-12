def is_shuffle(s1,s2,s3):
    if (len(s1) != len(s2) or len(s1)+len(s2) != len(s3)):
        return False
    for i in xrange(len(s1)):
        if (s1[i] != s3[i] or s2[i] != s3[i+1]):
            return False
        return True

print is_shuffle('abc','def','adbecf')
