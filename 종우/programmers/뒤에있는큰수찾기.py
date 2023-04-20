# 0420
# https://school.programmers.co.kr/learn/courses/30/lessons/154539

# 시간초과
def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        tmp = numbers[i+1:]
        nb = 1_000_001
        for tc in tmp:
            if tc > numbers[i]:
                nb = tc
                break
        if nb == 1_000_001:
            answer.append(-1)
        else:
            answer.append(nb)
        
    answer.append(-1)
    return answer