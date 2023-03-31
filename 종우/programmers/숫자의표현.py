# 1008_1
# 숫자의 표현
# https://school.programmers.co.kr/learn/courses/30/lessons/12924

# 내 풀이
def solution(n):
    answer = 0
    left = 0
    right = 1
    add = 1
    while True:
        if (left == right):
            answer += 1
            break
        elif (right>n):
            break
        if add == n:
            answer += 1
            add -= left 
            left += 1
            right += 1
            add += right
        elif add < n:
            right += 1
            add += right
        elif add > n:
            add -= left
            left += 1
    
    return answer

# 다른 풀이
def expressions(num):
    answer = 0
    for i in range(1, num + 1):
        s = 0
        while s < num:
            s += i
            i += 1
        if s == num:
            answer += 1
    return answer