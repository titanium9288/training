import sys

input = sys.stdin.readline


def is_in_circle(cx, cy, x1, y1, r):
    return (x1 - cx) ** 2 + (y1 - cy) ** 2 < r**2


T = int(input())

for _ in range(T):
    start_x, start_y, end_x, end_y = map(int, input().split())
    count = 0

    N = int(input())

    for _ in range(N):
        circle_x, circle_y, r = map(int, input().split())

        start_inside = is_in_circle(circle_x, circle_y, start_x, start_y, r)
        end_inside = is_in_circle(circle_x, circle_y, end_x, end_y, r)

        if start_inside != end_inside:
            count += 1

    print(count)
