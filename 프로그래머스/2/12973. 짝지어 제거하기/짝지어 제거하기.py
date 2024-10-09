def solution(s):
    stack = []
    
    for i in s:
        stack.append(i)
        
        if stack[-2:] == [stack[-1]] * 2:
            stack.pop()
            stack.pop()
        
    
    return 0 if stack else 1