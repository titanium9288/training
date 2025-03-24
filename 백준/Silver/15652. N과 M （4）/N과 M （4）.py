def repeated_combination(start, path):
    if len(path) == M:
        print(*path)
        return

    for i in range(start, N + 1):
        repeated_combination(i, path + [i])


N, M = map(int, input().split())
repeated_combination(1, [])
