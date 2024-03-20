from collections import deque

queue = deque()
n, k = map(int, input().split())

queue.append(n)
visited = [0] * 100001

while queue:
    p = queue.popleft()

    if p == k:
        break

    for np in (p - 1, p + 1, p * 2):
        if not (0 <= np < 100001):
            continue
        if visited[np]:
            continue
        visited[np] = visited[p] + 1
        queue.append(np)

print(visited[k])