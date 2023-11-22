from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cities = [i.lower() for i in cities]
    cache = deque()
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    if len(cities) < cacheSize:
        for i in range(len(cities)):
            if cities[i] in cache:
                cache.remove(cities[i])
                cache.append(cities[i])
                answer += 1
            else:
                cache.append(cities[i])
                answer += 5
        return answer
    else:
        for i in range(cacheSize):
            if cities[i] in cache:
                cache.remove(cities[i])
                cache.append(cities[i])
                answer += 1
            else:
                cache.append(cities[i])
                answer += 5

    for i in range(cacheSize, len(cities)):
        if cities[i] in cache:
            cache.remove(cities[i])
            cache.append(cities[i])
            answer += 1
        else:
            if len(cache) < cacheSize:
                cache.append(cities[i])
                answer += 5
            else:
                cache.popleft()
                cache.append(cities[i])
                answer += 5
            
    return answer