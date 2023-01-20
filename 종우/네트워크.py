# 0119_1
# https://school.programmers.co.kr/learn/courses/30/lessons/43162


# my fixed solution
# 1. counting trees in graph
def solution(n, computers):
    visited = []
    answer = 0
    
    for i in range(n):
        if i not in visited:
            q = [i]
            while(len(q) != 0):
                cur = q.pop(0)
                visited.append(cur)
                for j in range(n):
                    if computers[cur][j] == 1 and j not in visited:
                        q.append(j)
            answer += 1
    return answer


# 테케
[[1,0,0,0,0,0,1],[0,1,1,0,1,0,0],[0,1,1,1,0,0,0],[0,0,1,1,0,0,0],[0,1,0,0,1,1,0],[0,0,0,0,1,1,1],[1,0,0,0,0,1,1]]