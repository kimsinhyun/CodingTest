# 연구소
# 0330
# https://www.acmicpc.net/problem/14502


import sys

# 표준 입력을 파일로 설정하기 -> input.txt를 읽어들여옴
sys.stdin = open("test1.txt", "r")

# 표준 입력을 파일로 바꿨으므로, 
# input() 함수는 더이상 사용자 입력을 받지 않고, 지정된 입력 파일을 읽게 됨.
n,m = map(int, input().split())

# list comprehension을 이용해 이후의 입력값을 받아옴
arr = [list(map(int, input().split())) for _ in range(m)]
print(arr)


# visited = [[False]*m for _ in range(n)]

# n, m = map(int, input().split())
# board = [list(map(int, input.split())) for _ in range(n)]
# print(board)