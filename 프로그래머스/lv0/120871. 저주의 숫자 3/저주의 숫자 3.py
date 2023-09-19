def is3in(n):
    
    # 숫자가 3의 배수인가?
    if int(n) % 3 == 0:
        return True
    
    # 3이 포함되었는가?
    if "3" in str(n):
        return True
        
    return False

def no3(n):
    result = 0
    for i in range(1, n + 1):
        result += 1
        while is3in(result):
            result += 1
        
    return result

def solution(n):
    return no3(n)