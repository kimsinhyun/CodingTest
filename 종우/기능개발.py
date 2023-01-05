# 0104_1
# https://school.programmers.co.kr/learn/courses/30/lessons/42586

# 내 풀이
import math

def solution(progresses, speeds):
    answer = []
    dday = []
    for p, s in zip(progresses, speeds):
        pday = math.ceil((100-p)/s)
        dday.append(pday)
    
    nf = 1
    lt = dday.pop(0)
    for i in dday:
        if i <= lt:
            nf += 1
        else:
            answer.append(nf)
            nf = 1
            lt = i
    answer.append(nf)
    return answer

# 다른 풀이
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]