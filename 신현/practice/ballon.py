"""
https://www.acmicpc.net/problem/2346
"""

from collections import deque
temp = int(input())
temp_list = list(map(int, input().split(" ")))
dq = deque(enumerate(temp_list))

answer = deque()

while(len(dq) > 0):
    print(*dq)
    idx, next_idx = dq.popleft()
    answer.append(idx+1)
    if next_idx > 0:
        dq.rotate(-(next_idx-1))
    else:
        print(f"next_idx: {next_idx}")
        dq.rotate(-next_idx)

    
print(*answer)