N = int(input())
triangles = 0

for a in range(1, N // 3 + 1):
    # a를 고정하고, b를 루프 돌렸는데 N이 너무 크다.
    # 따라서 전략을 변경

    # b의 최소값과 최대값을 유효한 범위 내에서 미리 계산하기
    # a + b > c 여야 하므로, b의 하한선 유도
    b_min = (N - 2 * a) // 2 + 1

    # a 이상이어야 중복하지 않음이 성립
    b_min = max(a, b_min)

    # b가 c보다 크지 않아야 중복을 피할 수 있는 상황에서,
    # c = b일 때, b <= N - a - b 여야 하므로,
    # b의 최대값을 유도
    b_max = (N - a) // 2

    if b_max >= b_min:
        triangles += b_max - b_min + 1

print(triangles)
