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

# 시간초과 2
def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    visited = [0] * n
    
    for i in range(1, n):
        for j in range(i):
            if not visited[j]:
                if numbers[j] < numbers[i]:
                    visited[j] = 1
                    answer[j] = numbers[i]
        
    return answer

# solved using stack
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers)):
        while stack and numbers[i] > numbers[stack[-1]]:
            update = stack.pop()
            answer[update] = numbers[i]
        stack.append(i)
    
    return answer