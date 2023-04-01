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
    infected = True
    arr = copy.deepcopy(arrog)
    while infected:
        infected = False
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == 2:
                    y1, y2, x1, x2 = i-1, i+1, j-1, j+1
                    toinfect = [(y1, j), (y2, j), (i, x1), (i, x2)]
                    for ti in toinfect:
                        if ti[0] >= 0 and ti[0] < len(arr) and ti[1] >= 0 and ti[1] <len(arr[i]) and arr[ti[0]][ti[1]] != 1 and arr[ti[0]][ti[1]] != 2:
                            arr[ti[0]][ti[1]] = 2
                            infected = True
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