def primes_sieve(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5),2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
        print sieve
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def is_prime(n):
    """
    Returns if a given number is prime. If the number (n) is 1,2,3,5,7 returns
    true. If the number is even or odd returns false.
    """
    if n in [1,2,3,5,7]: return True
    if (n % 2 == 0 or n % 3 == 0): return False
    i = 5
    while i <= int(n**0.5):
        if n % i == 0: return False
        if n % (i+2) == 0: return False
        i += 6
    return True
