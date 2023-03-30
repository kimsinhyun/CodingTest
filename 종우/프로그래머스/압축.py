# 0122_1
# https://school.programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    dictionary = {}
    answer = []
    longest = 1
    trk = 27
    tmp = ""
    for j, ch in enumerate(msg):
        if len(tmp) < longest:
            tmp += ch
            continue
        for i in range(longest):
            lk = tmp[:longest-i]
            if len(lk) == 1:
                answer.append(ord('A')-64)
                tmp = ""
                trk += 1
            elif lk in dictionary:
                answer.append(dictionary[lk])
                tmp = tmp[longest-i:]
                
    return answer


# 다른 풀이
def solution(msg):
    dictionary = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    answer = []
    iter = 0
    tmp = msg[0]

    while iter != len(msg):
        if tmp in dictionary:
            if iter != len(msg)-1:
                iter += 1
            else:
                answer.append(dictionary.index(tmp)+1)
                break
            tmp += msg[iter]
        else:
            dictionary.append(tmp)
            answer.append(dictionary.index(tmp[:-1])+1)
            tmp = msg[iter]

    return answer

# 깔끔한 다른 풀이
def solution(msg):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {k:v for (k,v) in zip(alphabet, list(range(1,27)))}
    answer = []

    while True:
        if msg in d:
            answer.append(d[msg])
            break
        for i in range(1, len(msg)+1):
            if msg[0:i] not in d:
                answer.append(d[msg[0:i-1]])
                d[msg[0:i]] = len(d)+1
                msg = msg[i-1:]
                break

    return answer