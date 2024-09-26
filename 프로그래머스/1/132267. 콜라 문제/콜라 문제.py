def solution(a, b, n):
    answer = 0
    
    while n >= a:
        new = (n // a) * b
        answer += (n // a) * b
        n = (n % a) + new

    return answer