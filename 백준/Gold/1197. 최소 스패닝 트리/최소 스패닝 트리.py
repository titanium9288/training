import heapq
import sys
sys.setrecursionlimit(10**6)

# Union - Find
# 해당 노드의 루트를 찾기.
# 재귀적으로 반복하니, 값을 저장해두면 시간 단축
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


# 두 노드의 루트를 같게 만든다.
# 일관성 있게 합쳐야 문제가 생기지 않음
def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y


V, E = map(int, input().split())
edges = []

# Union-Find를 위한 list
parent = [i for i in range(V + 1)]

for _ in range(E):
    start, end, cost = map(int, input().split())

    # heap 을 이용하면 cost 순서로 정렬이 간단하다.
    # 크루스칼 알고리즘 이용하기
    heapq.heappush(edges, (cost, start, end))

# 누적 비용 계산
total_cost = 0

while edges:
    cost, start, end = heapq.heappop(edges)

    # 루트가 같다면 사이클이 생성되므로 추가하지 않음
    if find(start) == find(end):
        continue

    union(start, end)
    total_cost += cost

print(total_cost)
