from collections import deque
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
graph = {i: [] for i in range(1, V + 1)}

for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 케빈 베이컨의 수가 가장 작은 사람 구하기
min_user = 0
min_KB = float("inf")

# 모든 user에 대해 BFS를 돌려서 케빈 베이컨 수 구하기
for user in range(1, V + 1):
    distance = [-1] * (V + 1)
    distance[user] = 0
    queue = deque([user])

    # BFS
    while queue:
        u = queue.popleft()

        for v in graph[u]:
            if distance[v] != -1:
                continue

            distance[v] = distance[u] + 1
            queue.append(v)

    KB = sum(distance[1:])
    if min_KB > KB:
        min_user = user
        min_KB = KB

print(min_user)
