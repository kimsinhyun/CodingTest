# 0220
# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# 해쉬 

# 내 풀이
def solution(participant, completion):
    answer = ''
    ppl = {}
    for p in participant:
        if p not in ppl:
            ppl[p] = 1
        else:
            ppl[p] += 1
    for p in completion:
        ppl[p] += 1
    for p in ppl:
        if ppl[p] % 2 != 0:
            return p
    return answer

