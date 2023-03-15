from collections import deque
from os import error

# Number of Testcace
T = int(input())

for _ in range(T):
    # Function
    p = input()
    
    # Length of list
    n = int(input())

    # List
    number_list = deque(input()[1:-1].split(","))

    # Check Reverse
    check_reverse = False
    
    # Check Error
    check_error = False

    # Calc
    for func in p:        
        if func == "R":
            check_reverse = not check_reverse
        if func == "D":
            if len(number_list) == 0 or number_list[0] == '':
                print("error")
                check_error = True
                break
            
            if check_reverse:
                number_list.pop()
            else:
                number_list.popleft()       
    # Output  
    if check_error:
        continue
    else:
        if check_reverse:
            number_list.reverse()
        print("["+",".join(list(number_list))+"]")