from collections import deque

def solution(cacheSize, cities):
    cities = list(map(lambda x: x.lower(), cities))
    len_cities = len(cities)
    cache = deque()
    answer = 0
    
    for city in cities:
        if city in cache:
            cache.remove(city)
            answer += 1
        else:
            answer += 5
            
        cache.append(city)
    
        if len(cache) > cacheSize:
            cache.popleft()
    
    return answer