# 연구소
# 0330
# https://www.acmicpc.net/problem/14502

import sys

sys.stdin = open("test1.txt", "r")
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

"""
simulate expansion
count safe zones
"""

infected = True
while infected:
    infected = False
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 2 and i<0:
                pass
                


print(arr)

def countSafe(arr):
    safezones = 0
    for s in arr:
        safezones += s.count(0)
    return safezones