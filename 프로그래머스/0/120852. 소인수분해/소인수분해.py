def sieve(n):
    if n < 2:
        return []
    
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
                
    return [i for i in range(2, n + 1) if primes[i]]


def solution(n):
    return [i for i in sieve(n) if n % i == 0]