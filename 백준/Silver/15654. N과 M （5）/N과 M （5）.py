def NM5(path, visit):
    if len(path) == M:
        print(*path)
        return

    for i in range(len(numbers)):
        if visit[i]:
            continue
        visit[i] = True
        NM5(path + [numbers[i]], visit)
        visit[i] = False


N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
NM5([], [False] * N)