# 0220
# https://school.programmers.co.kr/learn/courses/30/lessons/42579
# 해쉬

def solution(genres, plays):
    answer = []
    playno = {}
    gp = list(zip(genres, plays, (i for i in range(len(genres)))))
    for i, j, x in gp:
        if i not in playno:
            playno[i] = j
        else:
            playno[i] += j
            
    gp.sort(key=lambda x: x[1], reverse=True)
    gp.sort(key=lambda x: x[0], reverse=True)
    
    tmp = ''
    skip = False
    for k in gp:
        if not skip and tmp != k[0]:
            answer.append(k[2])
            tmp = k[0]
        elif not skip and tmp == k[0]:
            answer.append(k[2])
            skip = True
        elif tmp==k[0] and skip:
            continue
        elif tmp!=k[0] and skip:
            answer.append(k[2])
            skip = False
            tmp = k[0]
    
    return answer