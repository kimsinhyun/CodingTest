# 0424
# https://school.programmers.co.kr/learn/courses/30/lessons/68936

def count(arr, x, y, length):
    cnt = [0,0]
    if length == 1:
        cnt[arr[y][x]] = 1
        return cnt
    
    n = arr[y][x]
    for i in range(length):
        for j in range(length):
            if arr[y+i][x+j] != n:
                break
        else:
            continue
        break
    else:
        cnt[arr[y][x]] = 1
        return cnt
    
    dx = [0, 1, 0, 1]
    dy = [0, 0, 1, 1]
    nlength = length//2
    for i in range(4):
        tmp = count(arr, x + dx[i]*nlength, y + dy[i]*nlength, nlength)
        cnt[0] += tmp[0]
        cnt[1] += tmp[1]
    return cnt
    

def solution(arr):
    answer = count(arr, 0, 0, len(arr))
    
    return answer