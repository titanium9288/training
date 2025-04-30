from collections import defaultdict
import sys

input = sys.stdin.readline


# Union - Find
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return

    if size[root_x] < size[root_y]:
        parent[root_x] = root_y
        size[root_y] += size[root_x]
    else:
        parent[root_y] = root_x
        size[root_x] += size[root_y]


T = int(input())

for _ in range(T):
    F = int(input())
    parent = defaultdict(lambda: None)
    size = defaultdict(int)
    answer = []

    for i in range(F):
        u, v = input().split()

        # 등장 여부 확인 후 초기화
        if parent[u] is None:
            parent[u] = u
            size[u] = 1

        if parent[v] is None:
            parent[v] = v
            size[v] = 1

        union(u, v)
        answer.append(str(size[find(u)]))

    print("\n".join(answer))
