N = int(input())
shirts = list(map(int, input().split()))
T, P = map(int, input().split())

print(sum(map(lambda x: (x // T) + (1 if x % T else 0), shirts)))
print(N // P, N % P)
