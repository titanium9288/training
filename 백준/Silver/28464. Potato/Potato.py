from collections import deque

N = int(input())
dishes = deque(sorted(map(int, input().split())))

S, P = 0, 0
for i in range(N):
    if i % 2:
        S += dishes.popleft()
    else:
        P += dishes.pop()

print(S, P)