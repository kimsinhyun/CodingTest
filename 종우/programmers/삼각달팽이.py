# 0428
# https://school.programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    answer = []
    triangle = []
    mv = [(0, 1), (1, 0), (-1, -1)]
    
    length = 0
    for i in range(n):
        length += (i+1)
        triangle.append([0]*(i+1))
        
    x = 0
    y = 0
    cnt = 1
    dir = 'down'
    for i in range(n, 0, -1):
        for j in range(i):
            if i == n and j == 0:
                continue
            triangle[y][x] = cnt
            cnt += 1
            if dir == 'down':
                x += mv[0][0]
                y += mv[0][1]
            elif dir == 'right':
                x += mv[1][0]
                y += mv[1][1]
            elif dir == 'up':
                x += mv[2][0]
                y += mv[2][1]
        if dir == 'down':
            dir = 'right'
        elif dir == 'right':
            dir = 'up'
        elif dir == 'up':
            dir = 'down'
    triangle[y][x] = cnt
    
    for i in triangle:
        for j in i:
            answer.append(j)
    
    return answer