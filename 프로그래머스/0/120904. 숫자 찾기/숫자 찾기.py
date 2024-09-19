def solution(num, k):
    num = str(num)
    
    for i in range(len(num)):
        if str(k) == num[i]:    
            return i + 1
    return -1
    