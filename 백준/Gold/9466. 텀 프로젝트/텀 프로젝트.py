import sys

sys.setrecursionlimit(10**6)


def dfs(current, dfs_id):
    if visited[current] == dfs_id:
        # 실제로 루프가 들어간 부분만 따로 빼야함.
        idx = path.index(current)
        return path[idx:]
    elif visited[current] != -1 and visited[current] != dfs_id:
        return None

    visited[current] = dfs_id
    path.append(current)

    neighbor = students[current]
    result = dfs(neighbor, dfs_id)

    path.pop()
    if result:
        return result

    return None


T = int(input())

for _ in range(T):
    N = int(input())
    students = [0] + list(map(int, input().split()))

    visited = [-1] * (N + 1)
    selected = set()
    dfs_id = 1

    for i in range(1, N + 1):
        if visited[i] != -1:
            continue
        
        # path를 전역으로 관리해서 메모리 절약
        path = [i]
        loop = dfs(i, dfs_id)

        if loop is not None:
            selected.update(loop)

        dfs_id += 1

    print(N - len(selected))
