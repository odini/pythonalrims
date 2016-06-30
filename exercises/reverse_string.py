# Recursive
def rec_reverse(text):
    if not len(text):
        return text
    return reverse(text[1:]) + text[0]

#Using extra buffer
def iter_reverse(text):
    result = []
    for i in xrange(len(text),0,-1):
        result.append(text[i-1])
    return ''.join(result)

#In place
def reverse_string(s):
    s_list = list(s)
    size = len(s_list)
    mid = size/2

    for i in xrange(0,mid):
        s_list[i], s_list[size-i-1] = s_list[size-i-1], s_list[i]

    return ''.join(s_list)

print reverse_string('odinl')
