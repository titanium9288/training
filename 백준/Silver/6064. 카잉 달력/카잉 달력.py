from math import lcm
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    LCM = lcm(M, N)

    for i in range(x, LCM + 1, M):
        if i % N == y % N:
            print(i)
            break
    else:
        print(-1)
