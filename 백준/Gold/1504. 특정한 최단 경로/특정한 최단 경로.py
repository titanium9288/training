import heapq


# 다익스트라
def dijkstra(start, N):
    distance = [float("inf") for _ in range(N + 1)]
    distance[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        dist_u, u = heapq.heappop(pq)

        if dist_u > distance[u]:
            continue

        for v, weight in graph[u]:
            dist_v = dist_u + weight

            if dist_v > distance[v]:
                continue

            distance[v] = dist_v
            heapq.heappush(pq, (dist_v, v))

    return distance


N, E = map(int, input().split())
graph = {i + 1: [] for i in range(N)}

for _ in range(E):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    graph[end].append((start, cost))

v1, v2 = map(int, input().split())

# 특정 지점부터 모든 점에 대해 경로 계산
dist_from_start = dijkstra(1, N)
dist_from_v1 = dijkstra(v1, N)
dist_from_v2 = dijkstra(v2, N)

# 경로 합치기
route1 = dist_from_start[v1] + dist_from_v1[v2] + dist_from_v2[N]
route2 = dist_from_start[v2] + dist_from_v2[v1] + dist_from_v1[N]

# 더 짧은 경로를 택하기
result = min(route1, route2)

# 만약 선택한 경로가 둘 다 존재하지 않는다면
if result == float("inf"):
    print(-1)
else:
    print(result)
