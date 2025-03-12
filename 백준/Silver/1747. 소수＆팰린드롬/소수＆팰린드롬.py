def palindrome_sieve(n):
    if n < 2:
        return []

    primes = [True] * (n + 1)  
    primes[0] = primes[1] = False  

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False


    return [i for i in range(n + 1) if primes[i] and str(i) == str(i)[::-1]]

primes = palindrome_sieve(1003001)
N = int(input())

for prime in primes:
    if N <= prime:
        print(prime)
        break
