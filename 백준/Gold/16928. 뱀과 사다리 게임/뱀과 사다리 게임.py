from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = defaultdict(list)
warp = {}

for _ in range(N + M):
    x, y = map(int, input().split())
    warp[x] = y

for i in range(1, 100):
    for dice in range(1, 7):
        move = i + dice

        if move > 100:
            continue

        if move in warp:
            move = warp[move]

        graph[i].append(move)

visited = [0] * 101
queue = deque([(1, 0)])
visited[1] = True

# BFS
while queue:
    node, roll = queue.popleft()

    for neighbor in graph[node]:

        if visited[neighbor]:
            continue

        visited[neighbor] = roll + 1
        queue.append((neighbor, roll + 1))

print(visited[100])
