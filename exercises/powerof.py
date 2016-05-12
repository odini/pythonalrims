# Find if a number is a power of other number

def powerof(num,x):
    while num != 1:
        if num % x:
            return False
        num /= x
    return True

print powerof(27,3)
