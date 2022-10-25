def solution(numbers, target):
    from collections import deque
    answer = 0
    n_len = len(numbers)
    q = deque([  [0,numbers[0]] , [0,-numbers[0]] ])
    print(q)
    while q:
        idx, t_val = q.popleft()
        idx+=1
        print(idx)
        if(idx < n_len):
            q.append([idx, t_val + numbers[idx]])
            q.append([idx, t_val - numbers[idx]])
        else:
            if t_val == target:
                answer+=1
    return answer