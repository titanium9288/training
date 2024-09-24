def get_rotations(s):
    return [(s+s)[i:i + len(s)] for i in range(len(s))]

def is_valid_braket(s):
    braket_stack = []
    braket_dict = {"{" : "}", "[": "]", "(" : ")"}
    
    for i in s:
        if i in ("{", "[", "("):
            braket_stack.append(i)
        if i in ("}", "]", ")"):
            if not braket_stack:
                return False
            if i != braket_dict[braket_stack.pop()]:
                return False
            
    
    return False if braket_stack else True

def solution(s):
    answer = 0
    
    for i in get_rotations(s):
        if is_valid_braket(i):
            answer += 1
            
    return answer