from collections import deque

K, N = map(int, input().split())
wine_list = deque(sorted(map(int, input().split())))
prev_wine = 0
result = 0

for i in range(N):
    if i % 2 == 0:
        current_wine = wine_list.pop()
        result += current_wine - prev_wine
    else:
        current_wine = wine_list.popleft()
    prev_wine = current_wine

print(result)