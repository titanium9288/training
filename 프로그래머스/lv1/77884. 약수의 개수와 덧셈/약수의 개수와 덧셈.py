def find_divisor(n):
    count = 1
    for i in range(1, int(n ** 1/2) + 1):
        if n % i == 0:
            count += 1
    return count

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        divisor = find_divisor(i)
        answer += i if divisor % 2 == 0 else (-1 * i)
    return answer