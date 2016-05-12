def rec_reverse(text):
    if not len(text):
        return text
    return reverse(text[1:]) + text[0]

def iter_reverse(text):
    result = []
    for i in xrange(len(text),0,-1):
        result.append(text[i-1])
    return ''.join(result)

print rec_reverse('odin')
