# 0305
# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    x = 0
    y = 0
    for size in sizes:
        width = size[0]
        height = size[1]
        if width > height:
            if width > x:
                x = width
            if height > y:
                y = height
        else:
            if height > x:
                x = height
            if width > y:
                y = width
        
    return x * y