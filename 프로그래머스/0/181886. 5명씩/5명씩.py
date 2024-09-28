def solution(names):
    return [names[i] for i in range(len(names)) if i % 5 == 0]