def solution(s):
    answer = 0
    
    while s:
        x = s[0]
        num_x = 1
        not_x = 0
        
        for i in range(1, len(s)):
            if s[i] == x:
                num_x += 1
            else:
                not_x += 1
            
            if num_x == not_x:
                s = s[i + 1:]
                break
        
        if num_x != not_x:
            s= ''
                
        answer += 1
    
    return answer