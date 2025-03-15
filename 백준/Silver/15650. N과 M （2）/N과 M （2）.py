def combination (start, path):
    if len(path) == M:
        print(*path)
        return
    
    for i in range(start, N + 1):
        combination(i+1, path + [i])
    

N, M = map(int, input().split())
combination(1, [])