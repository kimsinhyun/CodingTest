# https://www.acmicpc.net/problem/1920

import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int,input().split()))

M = int(input())
M_list = list(map(int,input().split()))

for m in M_list:
    print(1 if m in N_list else 0)
    