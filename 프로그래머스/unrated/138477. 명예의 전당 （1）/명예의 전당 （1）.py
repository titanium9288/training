def solution(k, scores):
    hof = []
    answer = []
    
    for score in scores:
        # 명예의 전당 크기보다 점수가 적을 경우
        if len(hof) < k:
            hof.append(score)
            
        else:
            lowest = hof.pop()
            # 가장 낮은 점수와 현재 점수중 높은 쪽을 추가
            hof.append(lowest if lowest > score else score)
        hof.sort(reverse=True)
        answer.append(hof[-1])
        
    return answer