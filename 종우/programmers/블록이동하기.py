# 0419
# https://school.programmers.co.kr/learn/courses/30/lessons/60063

from pprint import pprint

up = [0, -1]
down = [0, 1]
left = [-1, 0]
right = [1, 0]


def canmove(p1, p2, horizontal, board, move):
    pass

def solution(board):
    answer = 0
    nboard = [[] for _ in range(len(board) + 2)]
    nboard[0] = [1] * (len(board[0])+2)
    nboard[-1] = [1] * (len(board[0])+2)
    for i, b in enumerate(board):
        nboard[i+1] = [1] + b + [1]

    

    return answer

solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])