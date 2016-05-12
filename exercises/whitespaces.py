def whitespaces(text):
    result = []
    for i in xrange(len(text)):
        if text[i] != ' ':
            result.append(text[i])
    return ''.join(result)

print whitespaces('Python is great')
