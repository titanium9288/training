T = int(input())

for _ in range(T):
    V, E = map(int, input().split())
    F = E - V + 2

    print(F)
