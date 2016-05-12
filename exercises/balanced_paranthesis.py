#Balanced paranthesis including (),[],{}
def balance(s):
    opening = set('({[')
    match = [('(',')'),('{','}'),('[',']')]
    res = []
    for i in s:
        if i in opening:
            res.append(i)
        else:
            if not len(res):
                return False
            last = res.pop()
            if (last,i) not in match:
                return False
    return len(res) == 0

print balance('(()())')
