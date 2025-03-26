from collections import defaultdict, deque
import sys

input = sys.stdin.readline

N = int(input())
tree = defaultdict(list)
queue = deque()

for i in range(N - 1):
    A, B = map(int, input().split())

    tree[A].append(B)
    tree[B].append(A)

# 0번 인덱스 미사용
parent = [0] * (N + 1)
visited = [False] * (N + 1)

# root 부터 탐색 시작
queue.append(1)

while queue:
    current = queue.popleft()

    for neighbor in tree[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            parent[neighbor] = current
            queue.append(neighbor)

for i in parent[2:]:
    print(i)
