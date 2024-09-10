def solution(arr):
    # 길이가 2의 거듭제곱이 아닐때
    while (len(arr) & (len(arr) - 1)) != 0:
        arr.append(0)
    return arr