# 0130_1
# https://school.programmers.co.kr/learn/courses/30/lessons/12913

# 내 풀이 dfs
wanswer = 0
length = 0

def solution(land):
    global answer, length
    
    length = len(land)
    
    for i in range(4):
        dfs(land, 0, i, 0)
    
    return answer

def dfs(land, step, prev, score):
    global answer, length
    if step == length:
        if score > answer:
            answer = score
        return
    
    for i in range(4):
        if i != prev:
            dfs(land, step+1, i, score+land[step][i])

# dynamic programming
def solution(land):
    prev = land[0]
    tmp = [0]*4
    for i in range(1, len(land)):
        land[i][0] += max(land[i-1][1],land[i-1][2],land[i-1][3])
        land[i][1] += max(land[i-1][0],land[i-1][2],land[i-1][3])            
        land[i][2] += max(land[i-1][0],land[i-1][1],land[i-1][3])
        land[i][3] += max(land[i-1][0],land[i-1][1],land[i-1][2])
    return max(land[len(land)-1])