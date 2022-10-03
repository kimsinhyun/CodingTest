from collections import deque
def solution(people, limit):
    answer = 0
    q = deque(sorted(people, reverse=True))
    while q:
        if(len(q)>=2):
            # print(q)
            if (q[0] + q[-1] > limit):
                q.popleft()
                answer+=1
            else:
                q.pop()
                q.popleft()
                answer+=1
        else:
            q.pop()
            answer+=1    
            
    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70,  80, 50], 100))