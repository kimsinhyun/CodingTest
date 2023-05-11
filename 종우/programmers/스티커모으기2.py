# 0511
# https://school.programmers.co.kr/learn/courses/30/lessons/12971#
# dynamic programming

# initial solve using dp and two pointers (incorrect)
def solution(sticker):
    answer = 0
    length = len(sticker)
    n = length//2
    
    # even length
    if length%2 == 0:
        a = 0
        b = 0
        for i in range(n):
            a += sticker[2*i]
            b += sticker[2*i+1]
        answer = max(a,b)
    # odd length
    else:
        start = 0
        end = 2*(n-1)
        tmp = 0
        for i in range(n):
            tmp += sticker[2*i]
        answer = tmp
        for i in range(length):
            end = (end+2)%length
            tmp += sticker[end]
            tmp -= sticker[start]
            start = (start+2)%length
            answer = max(answer, tmp)
            
    return answer


