def solution(bandage, health, attacks):
    streak, turn = 0, 0
    max_health, attacks = health, attacks[::-1]
    
    while attacks:
        
        turn += 1
        
        # 공격 받았을 시
        if attacks[-1][0] == turn:
            health -= attacks[-1][1]
            attacks.pop()
            streak = 0
            
        else:
            streak += 1
            health = min(max_health, health + bandage[1])
            if streak == bandage[0]:
                health = min(max_health, health + bandage[2])
                streak = 0
        
        if health <= 0:
            return -1
    
    return health

    
    