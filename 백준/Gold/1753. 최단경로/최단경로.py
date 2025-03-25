import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
root = int(input())

graph = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 최단거리 배열 초기화.
dist = [float("inf")] * (V + 1)
dist[root] = 0

priority_queue = []
heapq.heappush(priority_queue, (0, root))

while priority_queue:
    weight, node = heapq.heappop(priority_queue)

    if weight > dist[node]:
        continue

    for neighbor, edge_weight in graph[node]:
        new_weight = edge_weight + weight

        if new_weight < dist[neighbor]:
            dist[neighbor] = new_weight
            heapq.heappush(priority_queue, (new_weight, neighbor))


for distance in dist[1:]:
    if distance == float("inf"):
        print("INF")
    else:
        print(distance)
