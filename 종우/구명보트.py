# 1012_2
# https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    trips = 0
    people.sort()
    l = 0
    r = len(people)-1
    while(l<=r):
        if people[l] + people[r] <= limit:
            trips += 1
            l += 1
            r -= 1
        else:
            trips += 1
            r -=1
    
    return trips