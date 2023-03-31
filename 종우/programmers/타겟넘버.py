# 0118_1
# https://school.programmers.co.kr/learn/courses/30/lessons/43165


# 내 풀이 178
def solution(numbers, target):
    answer = 0
    sums = [numbers[0], -numbers[0]]
    numbers.pop(0)
    for i in numbers:
        tmp = []
        for j in sums:
            tmp.append(j+i)
            tmp.append(j-i)
        sums = tmp
    return tmp.count(target)

# dfs 풀이
answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])
def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer
