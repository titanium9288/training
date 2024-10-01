import math

def number_to_position(n):
    if n == 0:
        n = 11
        
    x, y = (n - 1) % 3, (n - 1) // 3
    return [x, y]


def calculate_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    

def solution(numbers, hand):
    answer = ""
    left_hand, right_hand = [0, 3], [2, 3]
    
    for number in numbers:
        number_pos = number_to_position(number)
        x, y = number_pos
        
        left_distance = calculate_distance(number_pos, left_hand)
        right_distance = calculate_distance(number_pos, right_hand)
        is_left_hand = False
        
        
        # 왼손으로 누르는 경우
        if x == 0:
            left_hand = number_pos
            is_left_hand = True
        
        if x == 1:
            if left_distance < right_distance:
                is_left_hand = True
                
            elif left_distance == right_distance:
                if hand == "left":
                    is_left_hand = True
        
        
        # 손에 따른 동작처리
        if is_left_hand:
            answer += "L"
            left_hand = number_pos
        else:
            answer += "R"
            right_hand = number_pos
    
    return answer