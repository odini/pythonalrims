# Find SQRT without using **0.5
def sqrt(num):
    if num < 2:
        return num
    low, high = 0, (num/2)+1
    while low+1 < high:
        mid = (high + low)/2
        square = mid**2
        print mid
        if square == num:
            return mid
        elif square < num:
            low = mid
        else:
            high = mid
    return low

print sqrt(69)
