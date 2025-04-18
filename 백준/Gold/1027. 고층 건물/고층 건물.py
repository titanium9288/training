N = int(input())
buildings = list(map(int, input().split()))
max_view = 0

for i in range(N):
    view = 0

    # 건물 오른쪽
    max_slope = -float("inf")
    for j in range(i + 1, N):
        slope = (buildings[j] - buildings[i]) / (j - i)
        if slope > max_slope:
            view += 1
            max_slope = slope

    # 건물 왼쪽
    max_slope = -float("inf")
    for j in range(i - 1, -1, -1):
        slope = -(buildings[j] - buildings[i]) / (j - i)
        if slope > max_slope:
            view += 1
            max_slope = slope

    max_view = max(max_view, view)


print(max_view)