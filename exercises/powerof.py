# Find if a number is a power of other number

def power_of(num, x):
    while num != 1:
        if num % x:
            return False
        num /= x
    return True

print power_of(27,3)
