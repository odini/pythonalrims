#find and replace string without python built-in functions
def find(s,word):
    l = len(word)
    for i in xrange(len(s)):
        if s[i:i+l] == word:
            return i

def occ(s):
    in1=find(s,'not')
    in2=find(s,'poor')
    if (in1 and in2 and in2 > in1):
        return s[:in1] + 'good' + s[in2+4:]
    return s

print occ('The lyrics is not so poor')
