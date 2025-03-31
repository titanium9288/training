from collections import defaultdict, deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = defaultdict(list)

# 그래프 생성
for i in range(M):
    u, v = map(int, input().split())

    # 무방향 그래프니까 양쪽 연결
    graph[u].append(v)
    graph[v].append(u)

queue = deque()
is_visited = [False] * (N + 1)
answer = 0

for i in range(1, N + 1):

    # 방문했던 노드는 무시
    if is_visited[i]:
        continue

    # Cluster 체크
    queue.append(i)
    is_visited[i] = True
    answer += 1

    # BFS
    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if not is_visited[neighbor]:
                is_visited[neighbor] = True
                queue.append(neighbor)

print(answer)
