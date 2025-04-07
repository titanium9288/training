import heapq


N, M = map(int, input().split())

# 위상 정렬
graph = {i: [] for i in range(1, N + 1)}
indegree = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())

    # 진입 차수를 별도로 기록
    graph[A].append(B)
    indegree[B] += 1


# heapq를 사용하면 작은 순번이 앞으로 온다
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
