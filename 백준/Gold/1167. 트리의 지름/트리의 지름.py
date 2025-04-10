import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(current):
    max_dist = dist[current]
    max_node = current

    for next, cost in graph[current]:
        if dist[next] != -1:
            continue

        dist[next] = dist[current] + cost
        next_max_dist, next_max_node = dfs(next)

        if next_max_dist > max_dist:
            max_dist = next_max_dist
            max_node = next_max_node

    return max_dist, max_node


N = int(input())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(N):
    node = list(map(int, input().split()))
    u = node[0]

    i = 1
    while True:
        if node[i] == -1:
            break
        v, cost = node[i], node[i + 1]
        graph[u].append((v, cost))
        graph[v].append((u, cost))
        i += 2

# 첫 DFS로 지름의 한 점을 찾고
dist = [-1] * (N + 1)
dist[1] = 0
max_dist, max_node = dfs(1)

# 두 번째 DFS로 지름의 길이를 구하기
dist = [-1] * (N + 1)
dist[max_node] = 0
max_dist, max_node = dfs(max_node)

print(max_dist)
