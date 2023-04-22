# 0422
# https://school.programmers.co.kr/learn/courses/30/lessons/154538

# dfs solve (runtime error)
import math

answer = math.inf
found = False

def dfs(cur, step, y, n):
    global answer, found
    
    if cur == y:
        found = True
        if step < answer:
            answer = step
        return
    elif cur > y:
        return
    
    step += 1
    # plus n
    cur += n
    dfs(cur, step, y, n)
    cur -= n
    
    # multiply 2
    cur *= 2
    dfs(cur, step, y, n)
    cur = int(cur/2)
    
    # multiply 3
    cur *= 3
    dfs(cur, step, y, n)
    cur = int(cur/3)

def solution(x, y, n):
    # bfs backtracking while < y
    # dfs backtracking while < y
    dfs(x, 0, y, n)
    if not found:
        return -1
    return answer   


# dp solve using sets
def solution(x, y, n):
    answer = 0
    step = set()
    step.add(x)
    
    while step:
        if y in step:
            return answer
        
        nstep = set()
        for i in step:
            if i + n <= y:
                nstep.add(i+n)
            if i*2 <= y:
                nstep.add(i*2)
            if i*3 <= y:
                nstep.add(i*3)
        answer += 1
        step = nstep
    return -1