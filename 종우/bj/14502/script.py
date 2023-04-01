# 연구소
# 0330
# https://www.acmicpc.net/problem/14502

import sys
import copy

def countSafe(arr):
    safezones = 0
    for s in arr:
        safezones += s.count(0)
    return safezones

def infect(arrog):
    arr = copy.deepcopy(arrog)
    queue = []
    global m, n
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                queue.append((i,j))
    
    while queue:
        i, j = queue.pop(0)
        y1, y2, x1, x2 = i-1, i+1, j-1, j+1
        # toinfect = [(y1, j), (y2, j), (i, x1), (i, x2)]
        if y1 >= 0 and arr[y1][j] == 0:
            queue.append((y1, j))
            arr[y1][j] = 2
        if y2 < n and arr[y2][j] == 0:
            queue.append((y2, j))
            arr[y2][j] = 2
        if x1 >= 0 and arr[i][x1] == 0:
            queue.append((i, x1))
            arr[i][x1] = 2
        if x2 < m and arr[i][x2] == 0:
            queue.append((i, x2))
            arr[j][x2] = 2

    return countSafe(arr)

def block(arr, cnt):
    global bestcase
    if cnt == 3:
        safe = infect(arr)
        if safe > bestcase:
            bestcase = safe
        return

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                arr[i][j] = 1
                block(arr, cnt+1)
                arr[i][j] = 0

"""
simulate expansion -> change this using bfs
count safe zones
find optimal blocking spaces -> just all combinations
"""

sys.stdin = open("test1.txt", "r")
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
bestcase = 0

block (arr, 0)

print(bestcase)