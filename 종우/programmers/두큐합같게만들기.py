# 0505
# https://school.programmers.co.kr/learn/courses/30/lessons/118667

def solution(queue1, queue2):
    answer = 0
    whole = queue1 + queue2
    s1 = sum(queue1)
    s2 = sum(queue2)
    p1 = 0
    p2 = len(queue1)    
    goal = (s1+s2)//2
    
    for i in range(p2*4):
        if s1 > s2:
            s1 -= whole[p1]
            s2 += whole[p1]
            p1 = (p1+1) % (len(queue1)*2)
            answer += 1
        elif s1 < s2:
            s2 -= whole[p2]
            s1 += whole[p2]
            p2 = (p2+1) % (len(queue1)*2)
            answer += 1
        else:
            break
    else:
        return -1
    
    return answer