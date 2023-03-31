# 0222
# https://school.programmers.co.kr/learn/courses/30/lessons/12906

# 스택큐

from collections import deque

def solution(arr):
    answer = deque()
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    if len(arr) == 0:
        return []
    answer.append(arr[0])
    arr = arr[1:]
    for i in arr:
        if answer[-1] == i:
            continue
        answer.append(i)
    return list(answer)