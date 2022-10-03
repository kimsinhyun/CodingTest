import re
import sys
input = sys.stdin.readline


N = int(input())
board = [-1 for _ in range(N)]
visited = [False] * N
answer = 0

print(board)
print(visited)


def rule(r):
    for i in range(r):
        if (board[r] == board[i]) or (abs(board[r] - board[i]) == abs(r - i)):
            return False
    return True

def recur(row):
    global answer
    if(row == N):
        print(f"row = {row} ; board = {board} (o)")
        answer+=1
        return
    for r in range(N):
        board[row] = r
        print(f"row = {row} ; board = {board}")
        if(rule(row)):
            recur(row+1)
            
recur(0)
print(answer)
