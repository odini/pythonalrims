def duplicates(text):
    result = []
    for i in text:
        if i not in result:
            result.append(i)
    return ''.join(result)

print duplicates('ABBDCS')
