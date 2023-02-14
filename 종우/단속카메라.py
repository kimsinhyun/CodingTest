# 0214
# https://school.programmers.co.kr/learn/courses/30/lessons/42884


# my attempt
def solution(routes):
    # find positions where most cameras meet
    answer = 0
    score = [0]*60001
    
    for route in routes:
        for i in range(route[0], route[1]+1):
            score[i+30000] += 1
            
    while max(score)>0:
        greed = score.index(max(score))-30000
        answer += 1
        for route in routes:
            if route[0] <= greed <= route[1]:
                for i in range(route[0], route[1]+1):
                    score[i+30000] -= 1
        
    return answer


# answer
def solution(routes):
    # find positions where most cameras meet
    routes.sort(key=lambda x:x[1])
    camera = -30001
    answer = 0
    
    for route in routes:
        if  camera < route[0]:
            answer += 1
            camera = route[1]
        
    return answer