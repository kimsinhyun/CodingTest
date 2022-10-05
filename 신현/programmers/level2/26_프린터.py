def solution(priorities, location):
    from collections import deque
    answer = 0
    priorities=deque(priorities)
    temp = [False]*(len(priorities))
    temp[location] = True
    temp = deque(temp)
    
    while priorities:
        maxidx = priorities.index(max(priorities))
        priorities.rotate(-maxidx)
        temp.rotate(-maxidx)
        if(temp[0] == True):
            answer+=1
            break
        else:
            priorities.popleft()
            temp.popleft()
            answer+=1
            
    
    
    
    return answer