def sieve(n):
    if n < 2:
        return []

    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return [i for i in range(n + 1) if primes[i]]


a, b = map(int, input().split())
answer = 0

# sqrt(max) 까지의 체 구하기
primes = sieve(int(b**0.5) + 1)

# min~max 사이 구간을 bool 배열로 저장.
check = [False] * (b - a + 1)

for p in primes:
    p2 = p**2
    # a보다 크면서 p^2로 나눠 떨어지지 않는 수
    start = ((a + p2 - 1) // p2) * p2

    for i in range(start, b + 1, p2):
        check[i - a] = True
        
# False 의 갯수를 구하면 제곱ㄴㄴ수의 갯수
print(check.count(False))
