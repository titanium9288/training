def solution(angle):
    answer = (angle // 90) * 2 + (1 if angle % 90 else 0)
    return answer