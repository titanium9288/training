def count_k(X):
    total = 0
    for i in range(1, N + 1):
        total += min(X // i, N)
    return total


def binary_search(left, right):
    if left == right:
        return left

    mid = (left + right) // 2

    if count_k(mid) >= k:
        return binary_search(left, mid)
    else:
        return binary_search(mid + 1, right)


N = int(input())
k = int(input())

print(binary_search(1, N**2))
