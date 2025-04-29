import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

buses = defaultdict(list)

for _ in range(M):
    start, end, cost = map(int, input().split())
    buses[start].append((end, cost))

root, target = map(int, input().split())

# 최소비용 배열 초기화
dist = [float("inf")] * (N + 1)
dist[root] = 0

# 경로 추적
prev = [None] * (N + 1)


# 우선순위 큐
pq = []
heapq.heappush(pq, (0, root))

while pq:
    cost, node = heapq.heappop(pq)

    if cost > dist[node]:
        continue

    for next, edge_cost in buses[node]:
        new_cost = cost + edge_cost

        if new_cost < dist[next]:
            dist[next] = new_cost
            prev[next] = node
            heapq.heappush(pq, (new_cost, next))

print(dist[target])

path = []
while target is not None:
    path.append(target)
    target = prev[target]

print(len(path))
print(*reversed(path))
