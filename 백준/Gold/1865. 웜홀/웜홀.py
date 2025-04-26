from copy import deepcopy


TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split())
    edges = []

    # 도로
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))

    # 웜홀
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))

    # 음수 사이클 감지를 위해
    # 비용이 0인 가상의 노드를 하나 생성
    # 출발 지점을 0으로 해서, 0으로부터의 거리를 찾기

    for i in range(1, N + 1):
        edges.append((0, i, 0))

    # 벨만 포드
    dist = [0] + ([float("inf")] * N)

    for _ in range(N):
        for u, v, cost in edges:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost

    orig_dist = deepcopy(dist)

    # 음수 사이클 감지용으로 한 번 더 돌리기
    for u, v, cost in edges:
        if dist[v] > dist[u] + cost:
            dist[v] = dist[u] + cost

    if orig_dist != dist:
        print("YES")
    else:
        print("NO")
