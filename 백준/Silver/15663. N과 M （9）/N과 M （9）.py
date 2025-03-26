def NM9(path, visit):
    if len(path) == M:
        print(*path)
        return

    for i in range(len(numbers)):
        if visit[i]:
            continue
        if i > 0 and numbers[i] == numbers[i - 1] and not visit[i - 1]:
            continue

        visit[i] = True
        NM9(path + [numbers[i]], visit)
        visit[i] = False


N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
NM9([], [False] * N)