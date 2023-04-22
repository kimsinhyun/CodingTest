# 0422_3
# https://school.programmers.co.kr/learn/courses/30/lessons/12979

# initial solve
def solution(n, stations, w):
    answer = 0
    # mark all indexes with previous 4g
    # count additional 5g
    signal = [0] * (n+1)
    signal[0] = 1
    for s in stations:
        signal[s] = 1
        for i in range(1, w+1):
            if s - i > -1:
                signal[s-i] = 1
            if s + i < n:
                signal[s+i] = 1

    for i in range(n+1):
        if signal[i] == 0:
            for j in range(w*2+1):
                if i+j <= n+1:
                    signal[i+j] = 1
            answer += 1    

    return answer

# solve using ranges
def solution(n, stations, w):
    answer = 0
    ranges = []
    
    # get empty ranges
    begin = 1
    end = 1
    for s in stations:
        end = s - w
        if end-begin > 0: ranges.append(end-begin) 
        begin = s + w + 1
    end = n+1
    if end-begin > 0: ranges.append(end-begin) 
    
    # calculate addtional between the ranges
    for r in ranges:
        answer += r//(w*2+1)
        if r%(w*2+1) != 0: answer +=1

    return answer