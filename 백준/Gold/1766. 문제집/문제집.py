import heapq


N, M = map(int, input().split())

graph = {i: [] for i in range(1, N + 1)}
indegree = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    indegree[v] += 1

queue = []
for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(queue, i)

answer = []
while queue:
    current = heapq.heappop(queue)
    answer.append(current)

    for next in graph[current]:
        indegree[next] -= 1

        if indegree[next] == 0:
            heapq.heappush(queue, next)

print(*answer)
