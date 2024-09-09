def solution(arr):
    return arr.remove(min(arr)) or arr or [-1]