m, n = map(int, input().split())

sieve = [True] * (n + 1)
sieve[0] = False
sieve[1] = False

maximum = int(n**0.5)
for i in range(2, maximum+1):
    if sieve[i] == True:
        for j in range(2*i, n + 1, i):
            sieve[j] = False

print(*[prime for prime in range(m, n+1) if sieve[prime] == True])