#!/usr/bin/python

def primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5),2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
        print sieve
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def main():
    print primes(100)

if __name__ == '__main__':
    main()

