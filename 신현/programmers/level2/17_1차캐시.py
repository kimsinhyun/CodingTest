def solution(cacheSize, cities):
    from collections import deque
    cache = deque(maxlen=cacheSize)
    answer = 0
    for city in cities:
        city = city.lower()
        if(city in cache):
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            cache.append(city)
            answer+=5
                
    return answer