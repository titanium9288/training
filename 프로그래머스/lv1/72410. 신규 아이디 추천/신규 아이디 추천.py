import re

def solution(new_id):
    answer = new_id
    # step 1
    answer = answer.lower()

    # step 2
    answer = re.sub("[^a-zA-Z0-9_.-]", "", answer)

    # step 3
    answer = re.sub("[.]+", ".", answer)

    # step 4
    if answer[0] == ".":
        answer = answer[1::]
    if len(answer) != 0:
        if answer[-1] == ".":
            answer = answer [:-1:]
    
    # step 5
    if len(answer) == 0:
        answer = "a"
    
    # step 6
    if len(answer) >= 16:
        answer = answer[:15:]
        if answer[-1] == ".":
            answer = answer [:-1:]
    
    # step 7
    if len(answer) <= 2:
        answer = answer + (answer[-1] * (3 - len(answer)))

    return answer