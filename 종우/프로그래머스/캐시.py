# 1231_1
# https://school.programmers.co.kr/learn/courses/30/lessons/17680

# my initial 17-0.72ms
def solution(cacheSize, cities):
    answer = 0
    lru = []
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        lcity = city.lower()
        if len(lru) == cacheSize:
            if lcity in lru:
                lru.remove(lcity)
                lru.append(lcity)
                answer += 1
            else:
                lru.pop(0)
                lru.append(lcity)
                answer += 5
        else:
            if lcity in lru:
                lru.remove(lcity)
                lru.append(lcity)
                answer += 1
            else:
                lru.append(lcity)
                answer += 5
    return answer


# using deque
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time