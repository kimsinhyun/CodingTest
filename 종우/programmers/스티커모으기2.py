# 0511
# https://school.programmers.co.kr/learn/courses/30/lessons/12971#
# dynamic programming

# initial solve using brute force and two pointers (incorrect)
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

# solve using dynamic programming
def solution(sticker):
    answer = 0
    length = len(sticker)
    if length ==1:
        return sticker[0]
    
    dp = [[0]*length for _ in range(2)]
    dp[0][0] = sticker[0]
    dp[0][1] = sticker[0]
    dp[1][1] = sticker[1]
    
    for i in range(2, length-1):
        dp[0][i] = max(sticker[i]+dp[0][i-2], dp[0][i-1])
    for i in range(2, length):
        dp[1][i] = max(sticker[i]+dp[1][i-2], dp[1][i-1])
    
    answer = max(dp[0][length-2], dp[1][length-1])
    return answer