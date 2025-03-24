def NM12(start, path):
    if len(path) == M:
        print(*path)
        return

    for i in range(start, len(numbers)):
        NM12(i, path + [numbers[i]])


N, M = map(int, input().split())
numbers = sorted(list(set(map(int, input().split()))))
NM12(0, [])
