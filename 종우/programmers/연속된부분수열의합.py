# 0510
# https://school.programmers.co.kr/learn/courses/30/lessons/178870
# 투포인터

def solution(sequence, k):
    answer = [0, len(sequence)-1]
    start, end = 0, 0
    part = sequence[0]
    
    while True:
        print(start, end, part)
        if part == k:
            if end-1 - start < answer[1] - answer[0]:
                answer = [start, end-1]
            part += sequence[end]
            end +=1 
        else:
            if part < k:
                part += sequence[end]
                end += 1
            else:
                part -= sequence[start]
                start += 1
                
        if end == len(sequence):
            break
                
    return answer