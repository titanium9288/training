def calc_tree(H):
    total = 0
    for tree in trees:
        if tree > H:
            total += tree - H

    return total


N, M = map(int, input().split())
trees = list(map(int, input().split()))

# 이진탐색 구현
low, high = 0, max(trees)
answer = 0

while low <= high:
    mid = (low + high) // 2

    if calc_tree(mid) >= M:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)
