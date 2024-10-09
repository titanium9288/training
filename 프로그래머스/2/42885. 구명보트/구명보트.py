from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    
    while people:
        front = people.pop()
        
        if len(people): 
            back = people[0] 
            if limit >= front + back:
                people.popleft()
        
        answer += 1
    
    return answer