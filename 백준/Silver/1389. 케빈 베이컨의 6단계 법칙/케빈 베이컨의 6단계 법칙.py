import sys

input = sys.stdin.readline

V, E = map(int, input().split())
dist = [[0 if u == v else float("inf") for v in range(V + 1)] for u in range(V + 1)]
users = range(1, V + 1)

for _ in range(E):
    u, v = map(int, input().split())
    dist[u][v] = 1
    dist[v][u] = 1

# 플로이드-워셜
for k in users:
    for u in users:
        for v in users:
            dist[u][v] = min(dist[u][k] + dist[k][v], dist[u][v])

# 케빈 베이컨의 수가 가장 작은 사람 구하기
min_user = 0
min_KB = float("inf")

for user in users:
    KB = sum(dist[user][1:])
    if min_KB > KB:
        min_user = user
        min_KB = KB

print(min_user)
