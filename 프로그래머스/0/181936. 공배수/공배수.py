def solution(number, n, m):
    return int(((number % n) or (number % m)) == 0)