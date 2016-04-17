def reverse(text):
    if not len(text):
        return text
    return reverse(text[1:]) + text[0]

print reverse('odin')
