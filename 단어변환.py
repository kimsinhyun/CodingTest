# 0129_1
# https://school.programmers.co.kr/learn/courses/30/lessons/43163

minimum = 0
def solution(begin, target, words):
    global minimum
    if target not in words:
        return 0
    
    cur = begin
    cnt = 0
    visited = [0] * len(words)
    while cur != target:
        for i in range(len(words)):
            if isonediff(cur, words[i]) and not visited[i]:
                visited[i] = 1
                cnt += 1
                cur = words[i]
                break
    minimum = cnt
    print(cur)
    print(minimum)
    
    
    return minimum

def dfs(words, visited, cnt, cur):
    global minimum
    
    

def isonediff(a, b):
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
    if diff == 1:
        return True
    return False
    