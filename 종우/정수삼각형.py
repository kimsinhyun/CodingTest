# 0104_2
# https://school.programmers.co.kr/learn/courses/30/lessons/43105

# 내 풀이
def solution(triangle):
     
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0 :
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][-1]
            else:
                if triangle[i-1][j-1] > triangle[i-1][j]:
                    triangle[i][j] += triangle[i-1][j-1]
                else :
                    triangle[i][j] += triangle[i-1][j]
    answer = max(triangle[-1])
    return answer

# 다른 풀이

def solution(triangle):
    dp = []
    for t in range(1, len(triangle)):
        for i in range(t+1):
            if i == 0:
                triangle[t][0] += triangle[t-1][0]
            elif i == t:
                triangle[t][-1] += triangle[t-1][-1]
            else:
                triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
    return max(triangle[-1])