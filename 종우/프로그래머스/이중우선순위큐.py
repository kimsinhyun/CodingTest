# 0103_4
# https://school.programmers.co.kr/learn/courses/30/lessons/42628

# 내 풀이
def solution(operations):
    pq = []
    
    for i in operations:
        if i[0] == "I":
            pq.append(int(i.split()[1]))
        elif i[0] == "D":
            try:
                if i[2] == "-":
                    pq.remove(min(pq))
                else:
                    pq.remove(max(pq))
            except:
                pass
    
    if len(pq) == 0:
        return [0,0]
    else :
        return [max(pq), min(pq)]