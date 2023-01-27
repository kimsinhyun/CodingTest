# 0127
# https://school.programmers.co.kr/learn/courses/30/lessons/92341


#내 풀이
import math

def solution(fees, records):
    tracker = {}
    answer = []    
    
    for record in records:
        r = record.split(" ")
        if r[1] not in tracker:
            tracker[r[1]] = [translate(r[0])]
        else:
            tracker[r[1]].append(translate(r[0]))
        
    for track in tracker:
        if len(tracker[track]) % 2 != 0:
            tracker[track].append(23*60+59)
        answer.append([track])
        for i in range(0,len(tracker[track]),2):
            if i == 0:
                answer[-1].append(tracker[track][i+1]-tracker[track][i])
            else:
                answer[-1][1] += tracker[track][i+1]-tracker[track][i]
        answer[-1][1] = payment(answer[-1][1], fees)
            
    answer.sort(key= lambda time:int(time[0]))
    answer = [j for i, j in answer]
    
    return answer

def translate(time):
    hour, minute = time.split(":")
    return int(hour)*60 + int(minute)

def payment(t, fees):
    btime, bfee, atime, afee = fees
    if t <= btime:
        return bfee
    else:
        return bfee + math.ceil((t-btime)/atime)*afee