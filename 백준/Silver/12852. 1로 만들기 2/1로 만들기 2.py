from collections import defaultdict, deque

# 상태전이를 is_visited 에서만 관리
X = int(input())
queue = deque([X])
is_visited = defaultdict(list)

# BFS
while queue:
    current = queue.popleft()
    if current == 1:
        is_visited[1] += [1]
        print(len(is_visited[1]) - 1)
        print(*is_visited[1])
        break

    next_candidate = []

    if current % 3 == 0:
        next_candidate.append(current // 3)
    if current % 2 == 0:
        next_candidate.append(current // 2)
    if current - 1 > 0:
        next_candidate.append(current - 1)

    for next in next_candidate:
        if is_visited[next]:
            continue

        is_visited[next] = is_visited[current] + [current]
        queue.append(next)
