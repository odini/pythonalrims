#Balanced paranthesis
def balance(s):
    balanced = False
    res = []
    for i in s:
        if i == '(':
            res.append(i)
        else:
            if not res:
                return False
            else:
                res.pop()
    if not res: balanced = True
    return balanced

print balance('(()())')
