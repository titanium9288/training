from collections import deque
from itertools import combinations


def backtrack(a_set):
    result = set()
    result.add(tuple(sorted(a_set)))  # 중복 없이 저장

    for u in a_set:
        for neighbor in graph[u]:
            if neighbor not in a_set:
                a_set.add(neighbor)
                result |= backtrack(a_set)
                a_set.remove(neighbor)

    return result


def is_connected(area):
    start_node = list(area)[0]
    visited = {start_node}
    queue = deque([start_node])

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            # 이동 경로를 area에 있는 노드로 제한
            if neighbor not in area:
                continue
            if neighbor in visited:
                continue

            visited.add(neighbor)
            queue.append(neighbor)

    return visited == area


N = int(input())
population = [0] + list(map(int, input().split()))
graph = {i: [] for i in range(1, N + 1)}

for u in range(1, N + 1):
    v_list = list(map(int, input().split()))[1:]
    for v in v_list:
        graph[u].append(v)
        graph[v].append(u)

entire = set(range(1, N + 1))
min_diff = float("inf")

# combinations를 이용해 부분집합을 생성 후,
# BFS로 각자 연결 상태를 검증하기
for k in range(1, N // 2 + 1):
    for A in combinations(range(1, N + 1), k):
        A = set(A)
        B = entire - A

        if not is_connected(A):
            continue
        if not is_connected(B):
            continue

        # 인구 수 차이 계산 및 갱신
        sum_A = sum(population[i] for i in A)
        sum_B = sum(population[i] for i in B)

        diff = abs(sum_A - sum_B)
        min_diff = min(diff, min_diff)

if min_diff == float("inf"):
    print(-1)
else:
    print(min_diff)
