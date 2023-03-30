# 0105_1
# https://school.programmers.co.kr/learn/courses/30/lessons/42587

# 내 풀이
def solution(priorities, location):
    
    find = (priorities[location], location)
    x = list(zip(priorities, [i for i in range(len(priorities))]))
    tmp = []
    
    while len(x) != 0:
        if max(x)[0] == x[0][0]:
            tmp.append(x[0])
            x.pop(0)
        else:
            x.append(x[0])
            x.pop(0)     
            
    answer=tmp.index(find)+1
    return answer

# 다른사람 풀이
# The any() function returns True if any element of an iterable is True. If not, it returns False.

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer