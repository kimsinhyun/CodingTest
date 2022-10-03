import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
human_list = deque([i for i in range(1, N+1)])
answer = []

while human_list:
    human_list.rotate(-(K-1))
    answer.append(str(human_list.popleft()))
sys.stdout.write("<" + ", ".join(answer) + ">")
