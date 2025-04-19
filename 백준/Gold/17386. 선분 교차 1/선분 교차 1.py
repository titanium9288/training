def CCW(A, B, C):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    cross_product = x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3
    if cross_product == 0:
        return 0

    # return (cross_product > 0) - (cross_product < 0)
    return cross_product // abs(cross_product)


# C가 A-B 안에 있는가?
def on_segment(A, B, C):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    return min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2)


# 두 선의 교차 판정
def is_crossed(A, B, C, D):

    # 네 방향에 대해서 CCW 를 통해 방향 확인
    ccw1 = CCW(A, C, B)
    ccw2 = CCW(A, D, B)
    ccw3 = CCW(C, A, D)
    ccw4 = CCW(C, B, D)

    # 두 선이 일직선 위에 존재할 경우
    if ccw1 == ccw2 == ccw3 == ccw4 == 0:
        x1, y1 = A
        x2, y2 = B
        x3, y3 = C
        x4, y4 = D

        # 일직선에서 두 선의 범위가 겹치는가?
        if (
            max(x1, x2) >= min(x3, x4)
            and max(x3, x4) >= min(x1, x2)
            and max(y1, y2) >= min(y3, y4)
            and max(y3, y4) >= min(y1, y2)
        ):
            return 1

        # 한 점이 끝 점에 겹치는 경우
        # 처음엔 CCW로 판정했었는데,
        # CCW는 직선을 보장해도 선분을 보장하지 않는다. 실패 기록을 남김.
        if ccw1 == 0 and on_segment(A, B, C):
            return 1
        if ccw2 == 0 and on_segment(A, B, D):
            return 1
        if ccw3 == 0 and on_segment(C, D, A):
            return 1
        if ccw4 == 0 and on_segment(C, D, B):
            return 1

        return 0

    # 두 방향의 CCW중 하나라도 부호가 다를 경우 교차
    return int(ccw1 * ccw2 < 0 and ccw3 * ccw4 < 0)


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

A, B, C, D = (x1, y1), (x2, y2), (x3, y3), (x4, y4)

print(is_crossed(A, B, C, D))